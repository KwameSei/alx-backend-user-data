#!/usr/bin/env python3
"""
  Implementation of API session authentication.
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from uuid import uuid4
from models.user import User


class SessionAuth(Auth):
    """
      Class for Session Authentication
    """
    user_id_by_session_id = {}   # Dictionary of session_id: user_id

    def create_session(self, user_id: str = None) -> str:
        """
          Implement a Session ID for a user_id
        """
        if not user_id or isinstance(user_id, str) != str:  # if user_id is None
            return None

        session_id = str(uuid4())  # create session_id
        if not session_id:
            return None

        self.user_id_by_session_id[session_id] = user_id   # add to dictionary
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
          Returning a User ID based on a Session ID
        """
        if session_id is None or isinstance(session_id, str) != str:
            return None

        return self.user_id_by_session_id.get(session_id)   # return user_id

    def current_user(self, request=None):
        """
          Overloads Auth and retrieves the User instance for a request
        """
        if not request:
            return None
        session_id = self.session_cookie(request)  # get session_id from cookie
        if not session_id:
            return None
        user_id = self.user_id_for_session_id(session_id)  # get user_id
        if not user_id:
            return None
        return User.get(user_id)   # return User instance
