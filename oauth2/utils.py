import string
import urllib
import urlparse
from Crypto.Random import random

UNICODE_ASCII_CHARACTERS = (string.ascii_letters.decode('ascii') +
    string.digits.decode('ascii'))


def random_ascii_string(length):
    ''.join([random.choice(UNICODE_ASCII_CHARACTERS) for x in xrange(length)])


def query_params(url):
    """Return query parameters as a dict from the specified URL.

    :param url: URL.
    :type url: str
    :rtype: dict
    """
    return dict(urlparse.parse_qsl(urlparse.urlparse(url).query, True))


def build_url(base, additional_params=None):
    """Construct a URL based off of base containing all parameters in
    the query portion of base plus any additional parameters.

    :param base: Base URL
    :type base: str
    ::param additional_params: Additional query parameters to include.
    :type additional_params: dict
    :rtype: str
    """
    url = urlparse.urlparse(base)
    params = {}
    params.update(urlparse.parse_qsl(url.query, True))  # True preserves empty params
    if additional_params is not None:
        params.update(additional_params)

    return urlparse.urlunparse((url.scheme,
                                url.netloc,
                                url.path,
                                url.params,
                                urllib.urlencode(params),
                                url.fragment))
