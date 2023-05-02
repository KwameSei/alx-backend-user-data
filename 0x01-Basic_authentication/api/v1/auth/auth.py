#!/usr/bin/env python3
"""
  Implementation of API authentication.
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
      Class for authenticating users
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
          This method requires authentication for all routes except
          /status and /api/v1/unauthorized and /api/v1/forbidden
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
          This method handles authorization header
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
          This method handles current user
        """
        return None
