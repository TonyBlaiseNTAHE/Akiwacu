#!/usr/bin/python3

"""
subscription module
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Subscription(Base):
    """ class subscription"""
    __tablename__ = 'subscriptions'
    id = Column(Integer, primary_key=True, nullable=False)
    price = Column(Integer, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))  # Define foreign key relationship to the users table

    def to_dict(self):
        return {
            'id': self.id,
            'price': self.price,
            'start_date': self.start_date,
            'end_date': self.end_date,
        }
    
    def __repr__(self):
        return f'Subscription: {self.price}, {self.start_date}, {self.end_date}'

