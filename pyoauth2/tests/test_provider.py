from __future__ import absolute_import
import unittest
from pyoauth2.provider import AuthorizationProvider


class MockAuthorizationProvider(AuthorizationProvider):
    pass


class AuthorizationProviderTest(unittest.TestCase):

    def setUp(self):
        self.provider = MockAuthorizationProvider()

    def test_make_redirect_error_response(self):

        response = self.provider._make_redirect_error_response(
            'https://test.example.com/oauthredirect?param=1234',
            'some_error')
        self.assertEquals(302, response.status_code)
        self.assertEquals('https://test.example.com/oauthredirect?'
                          'param=1234&error=some_error',
                          response.headers['Location'])

    def test_make_json_error_response(self):

        response = self.provider._make_json_error_response('some_error')
        self.assertEquals(400, response.status_code)
        try:
            response_json = response.json()
        except TypeError:
            response_json = response.json
        self.assertEquals({'error': 'some_error'}, response_json)

    def test_get_authorization_code_invalid_response_type(self):

        response = self.provider.get_authorization_code('foo', 'client12345',
                                               'https://example.com/oauth')

        self.assertEquals(302, response.status_code)
        self.assertEquals('https://example.com/oauth?'
                          'error=unsupported_response_type',
                          response.headers['Location'])
