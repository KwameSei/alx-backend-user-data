#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound
from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """ Method that adds user to the database """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)  # Adds new User record to the database
        self._session.commit()   # Commits all changes
        return user  # Returns the new User object

    def find_user_by(self, **kwargs):
        """ Method that returns user found in database """
        if not kwargs:
            raise InvalidRequestError

        user = self.__session.query(User).filter_by(**kwargs).first()
        if not user:    # If no user found, raise NoResultFound
            raise NoResultFound

        return user
