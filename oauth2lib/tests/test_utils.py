from __future__ import absolute_import
import unittest
from oauth2lib import utils


class UtilsTest(unittest.TestCase):

    def setUp(self):
        self.base_url = 'https://www.myapp.com/some/path;hello?c=30&b=2&a=10'

    def test_random_ascii_string(self):
        """Test that random_ascii_string generates string of correct length."""
        code = utils.random_ascii_string(25)

        self.assertEquals(25, len(code))

    def test_url_query_params(self):
        """Test get query parameters dict."""
        result = utils.url_query_params(self.base_url)

        self.assertEquals(result, {'c': '30', 'b': '2', 'a': '10'})

    def test_url_dequery(self):
        """Test url dequery removes query portion of URL."""
        result = utils.url_dequery(self.base_url)

        self.assertEquals(result, 'https://www.myapp.com/some/path;hello')

    def test_build_url(self):
        """Test that build_url properly adds query parameters."""
        result = utils.build_url(self.base_url, {'b': 20})

        # Note param ordering and correct new value for b
        self.assertEquals(result, 'https://www.myapp.com/some/path;hello?a=10&c=30&b=20')
