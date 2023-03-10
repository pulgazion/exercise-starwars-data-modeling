import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    favorites = relationship('Favorite')

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    climate = Column(String(255), nullable=False)
    terrain = Column(String(255), nullable=False)
    population = Column(String(255), nullable=False)
    favorites = relationship('Favorite')

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    gender = Column(String(10), nullable=False)
    height = Column(String(255), nullable=False)
    mass = Column(String(255), nullable=False)
    hair_color = Column(String(255), nullable=False)
    eye_color = Column(String(255), nullable=False)
    birth_year = Column(String(255), nullable=False)
    favorites = relationship('Favorite')

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    planet_id = Column(Integer, ForeignKey('planets.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('characters.id'), nullable=True)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
