#!/usr/bin/python3

"""
movie module
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship


Base = declarative_base()

class Movie(Base):
    """ class movies"""
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(120),unique=True,  nullable=False)
    genre = Column(String(120), unique=True, nullable=False)
    release_date = Column(DateTime, nullable=False)
    duration = Column(Integer, nullable=False)
    
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'genre': self.genre,
            'release_date': self.release_date,
            'duration': self.duration
        }
    
    def __repr__(self):
        return f'Movie: {self.title}, {self.id}'
