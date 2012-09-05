from requests import Response
from cStringIO import StringIO
from . import utils


class Provider:
    """Base provider class for different types of OAuth 2.0 providers."""

    def _make_response(self, body='', headers=None, status_code=200):
        """Return a response object from the given parameters.

        :param headers: description
        :type headers: type
        :rtype: requests.Response
        """
        res = Response()
        res.status_code = status_code
        if headers is not None:
            res.headers.update(headers)
        res.raw = StringIO(body)
        return res


class AuthorizationProvider(Provider):
    """OAuth 2.0 authorization providers. This class manages authorization codes
    and access tokens. Certain methods MUST be overridden in a subclass, thus
    this class cannot be directly used as a provider.

    These are the methods that must be implemented in a subclass:

        validate_client_id(self, client_id)

        validate_client_secret(self, client_id, client_secret)

    Optionally, the following may be overridden to acheive desired behavior:

        @property
        token_length(self)

        generate_token(self)

    """

    @property
    def token_length(self):
        """Property method to get the length used to generate tokens.

        :rtype: int
        """
        return 40

    def generate_token(self):
        """Generate a random string token.

        :rtype: str
        """
        return utils.random_ascii_string(self.token_length)

    def get_authorization_code(self, client_id, redirect_uri):
        return self._make_response(headers=())

    def get_token(self, client_id, client_secret, redirect_uri, authorization_code):
        return self._make_response(headers=())

    def get_authorization_code_from_url(self, url):
        """Get authorization code response from URL. This method will
        ignore the domain and path of the request, instead
        automatically parsing the query string parameters.

        :param url: URL to parse for authorization information.
        :type url: str
        :rtype: requests.Response
        """
        params = utils.query_params(url)
        return self.get_authorization_code(**params)

    def get_token_from_url(self, url):
        """Get a token response from URL. This method will
        ignore the domain and path of the request, instead
        automatically parsing the query string parameters.

        :param url: URL to parse for authorization information.
        :type url: str
        :rtype: requests.Response
        """
        params = utils.query_params(url)
        return self.get_token(**params)


class ResourceProvider(Provider):
    pass
