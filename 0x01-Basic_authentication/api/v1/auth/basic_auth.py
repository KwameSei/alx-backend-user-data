#!/usr/bin/env python3
"""
  Implementation of API basic authentication.
"""
from api.v1.auth.auth import Auth
from base64 import b64decode
from typing import TypeVar
from models.user import User


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

    def user_object_from_credentials(self, user_email: str, user_pwd:
                                     str) -> TypeVar('User'):
        """
          Method that returns the User instance based on email and password.
        """
        if user_email is None or not isinstance(user_email, str):  # str only
            return None
        if user_pwd is None or not isinstance(user_pwd, str):  # str only
            return None
        try:
            users = User.search({'email': user_email})   # search for user
        except Exception:  # if search fails
            return None
        for user in users:   # for each user
            if not user.is_valid_password(user_pwd):
                return None
            else:
                return user
