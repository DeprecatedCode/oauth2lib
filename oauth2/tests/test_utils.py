from __future__ import absolute_import
import unittest
from oauth2 import utils


class UtilsTest(unittest.TestCase):

    def test_build_url(self):

        base = 'https://www.grapheffect.com/some/path;hello?c=30&b=2&a=10'

        result = utils.build_url(base, {'b': 20})

        # Note param ordering and correct new value for b
        self.assertEquals(result, 'https://www.grapheffect.com/some/path;hello?a=10&c=30&b=20')

