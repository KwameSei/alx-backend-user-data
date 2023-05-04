#!/usr/bin/env python3
"""
  Implementation of API session authentication.
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
      Class for Session Authentication
    """
    user_id_by_session_id = {}   # Dictionary of session_id: user_id

    def create_session(self, user_id: str = None) -> str:
        """
          Implement a Session ID for a user_id
        """
        if not user_id or isinstance(user_id) != str:  # if user_id is None
            return None

        session_id = str(uuid4())   # create session_id
        if not session_id:
            return None

        self.user_id_by_session_id[session_id] = user_id   # add to dictionary
        return session_id
    
    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
          Returning a User ID based on a Session ID
        """
        if not session_id or isinstance(session_id, str) != True:  # if session_id is None
            return None

        return self.user_id_by_session_id.get(session_id)   # return user_id
