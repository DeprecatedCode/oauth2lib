import requests
from . import utils


class Client(object):

    def __init__(self, client_id, client_secret, redirect_uri, \
                 authorization_uri, token_uri):
        """Constructor for OAuth 2.0 Client.

        :param client_id: Client ID.
        :type client_id: str
        :param client_secret: Client secret.
        :type client_secret: str
        :param redirect_uri: Client redirect URI: handle provider response.
        :type redirect_uri: str
        :param authorization_uri: Provider authorization URI.
        :type authorization_uri: str
        :param token_uri: Provider token URI.
        :type token_uri: str
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.redirect_uri = redirect_uri
        self.authorization_uri = authorization_uri
        self.token_uri = token_uri

    @property
    def default_response_type(self):
        return 'code'

    @property
    def default_grant_type(self):
        return 'authorization_code'

    def http_post(self, url, data=None):
        """POST to URL and get result as a response object.

        :param url: URL to POST.
        :type url: str
        :param data: Data to send in the form body.
        :type data: str
        :rtype: requests.Response
        """
        if not url.startswith('https://'):
            raise ValueError('Protocol must be HTTPS, invalid URL: %s' % url)
        return requests.post(url, data, verify=True)

    def get_authorization_code_uri(self, **params):
        """Construct a full URL that can be used to obtain an authorization
        code from the provider authorization_uri. Use this URI in a client
        frame to cause the provider to generate an authorization code.

        :rtype: str
        """
        if 'response_type' not in params:
            params['response_type'] = self.default_response_type
        params.update({'client_id': self.client_id,
                       'redirect_uri': self.redirect_uri})
        return utils.build_url(self.authorization_uri, params)

    def get_token(self, code, **params):
        """Get an access token from the provider token URI.

        :param code: Authorization code.
        :type code: str
        :return: Dict containing access token, refresh token, etc.
        :rtype: dict
        """
        params['code'] = code
        if 'grant_type' not in params:
            params['grant_type'] = self.default_grant_type
        params.update({'client_id': self.client_id,
                       'client_secret': self.client_secret,
                       'redirect_uri': self.redirect_uri})
        return self.http_post(self.token_uri, params).json()
