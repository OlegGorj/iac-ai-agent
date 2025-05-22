

class GatewayAuthenticator:
    """
    Handles authentication with the LLM gateway.
    Supports different authentication methods like API key, OAuth, etc.
    """

    def __init__(self, settings):
        """
        Initializes the GatewayAuthenticator with the provided settings.

        Args:
            settings (Settings): Configuration settings, including gateway URL and authentication method.
        """
        self.settings = settings
        self.auth_method = settings.gateway_auth_method
        self.gateway_url = settings.gateway_url

    def authenticate(self):
        """
        Authenticates with the gateway based on the configured authentication method.

        Returns:
            Credentials: An object containing the authentication credentials.

        Raises:
            ValueError: If the authentication method is not supported.
        """
        if self.auth_method == "api_key":
            return self._authenticate_with_api_key()
        # elif self.auth_method == "oauth":
        #     return self._authenticate_with_oauth()
        else:
            raise ValueError(f"Unsupported authentication method: {self.auth_method}")

    def _authenticate_with_api_key(self):
        """
        Authenticates with the gateway using an API key.

        Returns:
            Credentials: An object containing the API key.
        """
        api_key = self.settings.openai_api_key  # Assuming API key is stored in settings
        if not api_key:
            raise ValueError("API key not found in settings.")
        return Credentials(api_key=api_key)

    # def _authenticate_with_oauth(self):
    #     """
    #     Authenticates with the gateway using OAuth.
    #
    #     Returns:
    #         Credentials: An object containing the OAuth token.
    #     """
    #     # Implement OAuth flow here
    #     pass


class Credentials:
    """
    A simple class to hold authentication credentials.
    """
    def __init__(self, api_key: str = None, oauth_token: str = None):
        """
        Initializes the Credentials object with the provided credentials.

        Args:
            api_key (str, optional): The API key. Defaults to None.
            oauth_token (str, optional): The OAuth token. Defaults to None.
        """
        self.api_key = api_key
        self.oauth_token = oauth_token

