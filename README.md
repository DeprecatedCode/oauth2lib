oauth2lib
=========

## Python OAuth 2.0 Client and Provider Library

### Authorization Code Grant :: OAuth 2 Section 4.1

Authorization Request :: OAuth 2 Section 4.1.1

        [For browser apps this happens in the window]
        Request: GET /get_authorization_code
                        ?response_type=code
                        &client_id={CLIENT_ID}
                        &redirect_uri={REDIRECT_URI}
                        [&state={STATE}]
                        [&scope={SCOPE}]

        Response: HTTP 302
                    Location={REDIRECT_URI}
                        ?code={CODE}
                        &state={STATE}

        Error Response: HTTP 302
                    Location={REDIRECT_URI}
                        ?error=access_denied
                        &state={STATE}

Access Token Request :: OAuth 2 Section 4.1.3

        [Server side only]
        Request: GET /get_access_token
                        ?grant_type=authorization_code
                        &client_id={CLIENT_ID}
                        &client_secret={CLIENT_SECRET}
                        &redirect_uri={REDIRECT_URI}
                        &code={CODE}

        Response: HTTP 200
                    {
                       "access_token": "{ACCESS_TOKEN}",
                       "token_type": "{TOKEN_TYPE}",      // See OAuth 2 Section 7.1 Access Token Types
                       "expires_in": 3600,
                       "refresh_token": "{REFRESH_TOKEN}"
                     }

        Error Response: HTTP 400
                    {
                        "error": "access_denied",
                        "error_description": "User does not have access to the team."
                    }
