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
