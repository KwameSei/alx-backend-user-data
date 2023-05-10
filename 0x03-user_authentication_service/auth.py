#!/usr/bin/env python3
""" Creating auth module """
import bcrypt


def _hash_password(password: str) -> str:
    """ Method that accepts password argument and returns bytes """
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())  # Returns bytes
