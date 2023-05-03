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
    pass
