#!/usr/bin/python3
"""
Module that define the city class representing a city in MySQL database.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Represent a city from a MySQL database

    __tablename__(str): The name of the MySQL table to store cities.
    id (sqlalchemy.Integer): The cities's id
   name (sqlalchemy.String): The cities's name.
   """
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
