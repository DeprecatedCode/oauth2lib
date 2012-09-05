import requests
from . import utils


class Client:

    def __init__(self, client_id, client_secret, authorization_uri, \
                 token_uri, redirect_uri):
        self.client_id = client_id
        self.client_secret = client_secret
        self.authorization_uri = authorization_uri
        self.token_uri = token_uri
        self.redirect_uri = redirect_uri

    def get_url(self, url):
        """GET the contents of URL as a response object.

        :param url: URL to GET.
        :type url: str
        :rtype: requests.Response
        """
        if not url.startswith('https://'):
            raise ValueError('Protocol must be HTTPS, invalid URL: %s' % url)
        return requests.get(url, verify=True)

    def get_authorization_code(self, params=None):
        """"""
        if params is None:
            params = {}
        params.update({'client_id': self.client_id,
                       'redirect_uri': self.redirect_uri})
        return self.get_url(utils.build_url(self.authorization_uri, params))

    def get_token(self, params):
        return self.get_url(utils.build_url(self.token_uri, params))
