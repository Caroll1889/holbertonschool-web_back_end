#!/usr/bin/env python3
"""create user
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound


class DB:
    """DB Class"""

    def __init__(self):
        """Constructor
        """
        self._engine = create_engine("sqlite:///a.db", echo=False)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self):
        """Session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Add a new user in the DB
        """
        new = User(email=email, hashed_password=hashed_password)
        self._session.add(new)
        self._session.commit()
        return new

    def find_user_by(self, **kwargs) -> User:
        """Find a user in a DB"""
        user = self._session.query(User).filter_by(**kwargs).first()

        return user
