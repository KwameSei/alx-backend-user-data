#!/usr/bin/env python3
"""
  Implementation of API authentication.
"""
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """
      Class for authenticating users
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
          This method requires authentication for all routes except
          /status and /api/v1/unauthorized and /api/v1/forbidden
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            # Excluded paths is empty, so require auth for all paths
            # Excluded paths include /api/v1/status, /api/v1/unauthorized,
            return True

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/'):  # Add trailing slash if not
                # excluded_path += '/'
                excluded_path = excluded_path[:-1]  # Remove trailing slash
            if path == excluded_path or path.startswith(excluded_path):
                # Path is excluded, so do not require auth
                return False

        return True

        # if path[-1] != '/':
        #     path += '/'
        # if path in excluded_paths:
        #     return False
        # return True

    def authorization_header(self, request=None) -> str:
        """
          This method returns the value of the authorization header
        """
        if request is None or request == {}:  # If request is empty
            return None

        if 'Authorization' not in request.headers:  # If not Authorization
            return None

        return request.headers['Authorization']   # Return Authorization header

    def current_user(self, request=None) -> TypeVar('User'):
        """
          This method handles current user
        """
        return None
    
    def session_cookie(self, request=None):
        """
          Returns a cookie value from a request
        """
        if request is None or request == {}:  # If request is empty
            return None
        
        # return request.cookies.get('session_id')
        name = getenv('SESSION_NAME', '_my_session_id')  # Get session name
        return request.cookies.get(name)   # Return session_id cookie
