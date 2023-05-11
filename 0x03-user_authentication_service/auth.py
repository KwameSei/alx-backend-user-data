#!/usr/bin/env python3
""" Creating auth module """
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """ Method that accepts password argument and returns bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # Returns bytes


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """ Method that registers and returns a new user """

        try:
            user = self._db.find_user_by(email=email)  # Find user by email
            if user:   # If user exists, raise ValueError
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)   # Hash password
            user_add = self._db.add_user(email=email,
                                         hashed_password=hashed_password)

            return user_add
