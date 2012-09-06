from __future__ import absolute_import
import unittest
from oauth2.client import Client


class ClientTest(unittest.TestCase):

    def setUp(self):

        self.client = Client(client_id='some.client',
                             client_secret='ASDFGHJKL',
                             redirect_uri='https://example.com/oauth2redirect',
                             authorization_uri='https://grapheffect.com/oauth2/auth',
                             token_uri='https://grapheffect.com/oauth2/token')
