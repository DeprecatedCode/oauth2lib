from __future__ import absolute_import
import unittest
from oauth2.provider import AuthorizationProvider
from oauth2.client import Client

MOCK_CLIENT_ID = 'abc123456789'
MOCK_CLIENT_SECRET = 'MNBVCXZLKJHGFDSAPOIUYTREWQ'
MOCK_REDIRECT_URI = 'https://grapheffect.com/oauth_endpoint'


class MockClient(Client):

    def get_url(self, url):

        if url.startswith('https://example.com/auth'):
            return self.mock_provider_get_authorization_code(url)

        elif url.startswith('https://example.com/token'):
            return self.mock_provider_get_token(url)

        raise Exception('Test fail')


class MockAuthorizationProvider(AuthorizationProvider):
    """Implement an authorization OAuth2 provider for testing purposes."""

    def validate_client_id(self, client_id):
        return client_id == MOCK_CLIENT_ID

    def validate_client_secret(self, client_id, client_secret):
        return client_id == MOCK_CLIENT_ID and client_secret == MOCK_CLIENT_SECRET


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
        response = self.client.get_authorization_code()
