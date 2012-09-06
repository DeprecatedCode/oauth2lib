from __future__ import absolute_import
import unittest
from oauth2.provider import AuthorizationProvider


class MockAuthorizationProvider(AuthorizationProvider):
    pass


class AuthorizationProviderTest(unittest.TestCase):

    def setUp(self):

        self.provider = MockAuthorizationProvider()
