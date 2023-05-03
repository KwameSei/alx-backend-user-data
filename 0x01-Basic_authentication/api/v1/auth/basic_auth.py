#!/usr/bin/env python3
"""
  Implementation of API basic authentication.
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar


class BasicAuth(Auth):
    """
      Class for Basic Authentication
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
          Method that returns Base64 part of the Authorization header.
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):   # str only
            return None
        if not authorization_header.startswith('Basic '):   # Basic space
            return None
        return authorization_header[6:]   # 6 is len('Basic ')

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
          Method that returns decoded value of a Base64 string.
        """
        if base64_authorization_header is None:   # if auth is None
            return None
        if not isinstance(base64_authorization_header, str):   # str only
            return None
        try:
            decoded = b64decode(base64_authorization_header)  # decode
            return decoded.decode('utf-8')  # Decode header to utf-8
        except Exception:
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
          Method that returns the user email and password from the
          Base64 decoded value.
        """
        if decoded_base64_authorization_header is None:   # if auth is None
            return (None, None)

        if not isinstance(decoded_base64_authorization_header, str):
            return (None, None)

        if ':' not in decoded_base64_authorization_header:   # if : not in
            return (None, None)

        email, password = decoded_base64_authorization_header.split(':', 1)
        return (email, password)
