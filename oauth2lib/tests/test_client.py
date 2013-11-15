from __future__ import absolute_import
import unittest
from oauth2lib.client import Client
from oauth2lib import utils


class ClientTest(unittest.TestCase):

    def setUp(self):

        self.client = Client(client_id='some.client',
                             client_secret='ASDFGHJKL',
                             redirect_uri='https://example.com/oauth2redirect',
                             authorization_uri='https://myapp.com/oauth2/auth',
                             token_uri='https://myapp.com/oauth2/token')

    def test_get_authorization_code_uri(self):
        """Test client generation of authorization code uri."""
        uri = self.client.get_authorization_code_uri(state="app.state")

        # Check URI
        self.assertTrue(uri.startswith('https://myapp.com/oauth2/auth?'))

        # Check params
        params = utils.url_query_params(uri)
        self.assertEquals('code', params['response_type'])
        self.assertEquals('some.client', params['client_id'])
        self.assertEquals('https://example.com/oauth2redirect', params['redirect_uri'])
        self.assertEquals('app.state', params['state'])
