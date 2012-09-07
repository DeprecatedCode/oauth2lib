from __future__ import absolute_import
import unittest
from oauth2.provider import AuthorizationProvider
from oauth2.client import Client
from oauth2 import utils

MOCK_CLIENT_ID = 'abc123456789'
MOCK_CLIENT_SECRET = 'MNBVCXZLKJHGFDSAPOIUYTREWQ'
MOCK_REDIRECT_URI = 'https://grapheffect.com/oauth_endpoint'
MOCK_AUTHORIZATION_CODE = 'poiuytrewqlkjhgfdsamnbvcxz0987654321'


class MockClient(Client):

    def get_url(self, url):

        if url.startswith('https://example.com/auth'):
            return self.mock_provider_get_authorization_code(url)

        elif url.startswith('https://example.com/token'):
            return self.mock_provider_get_token(url)

        raise Exception('Test fail')

    def mock_get_authorization_code(self, **params):
        return self.get_url(self.get_authorization_code_uri(**params))


class MockAuthorizationProvider(AuthorizationProvider):
    """Implement an authorization OAuth2 provider for testing purposes."""

    def validate_client_id(self, client_id):
        return client_id == MOCK_CLIENT_ID

    def validate_client_secret(self, client_id, client_secret):
        return client_id == MOCK_CLIENT_ID and client_secret == MOCK_CLIENT_SECRET

    def validate_scope(self, client_id, scope):
        requested_scopes = scope.split()
        if client_id == MOCK_CLIENT_ID and requested_scopes == ['example']:
            return True
        return False

    def validate_authorization_code(self, client_id, code):
        return code == MOCK_AUTHORIZATION_CODE

    def validate_access(self):
        return True

    def persist_authorization_code(self, client_id, code, scope):
        pass

    def persist_token_information(self, client_id, code, scope, access_token,
                                  token_type, expires_in, refresh_token):
        pass


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.provider = MockAuthorizationProvider()
        self.client = MockClient(client_id=MOCK_CLIENT_ID,
                                 client_secret=MOCK_CLIENT_SECRET,
                                 authorization_uri='https://example.com/auth',
                                 token_uri='https://example.com/token',
                                 redirect_uri=MOCK_REDIRECT_URI + '?param=123')

        self.client.mock_provider_get_authorization_code = \
            self.provider.get_authorization_code_from_url

        self.client.mock_provider_get_token = \
            self.provider.get_token_from_url

    def test_get_authorization_code(self):
        """Test client's auth code URI generation and provider's response."""
        response = self.client.mock_get_authorization_code(scope='example')

        # Check status code
        self.assertEquals(302, response.status_code)

        # Check the non-query portion of the redirect URL
        redirect = response.headers['Location']
        self.assertEquals(utils.url_dequery(redirect), MOCK_REDIRECT_URI)

        # Check params in the redirect URL
        params = utils.url_query_params(redirect)
        self.assertEquals(3, len(params))
        self.assertEquals(40, len(params['code']))
        self.assertEquals('123', params['param'])
        self.assertEquals('example', params['scope'])

    def test_get_token_with_valid_authorization_code(self):
        """Test client's ability to get an access token from the provider."""
        data = self.client.get_token(code=MOCK_AUTHORIZATION_CODE,
                                     scope='example')

        self.assertEquals(40, len(data['access_token']))
        self.assertEquals(40, len(data['refresh_token']))
        self.assertEquals('Bearer', data['token_type'])
        self.assertEquals(3600, data['expires_in'])
