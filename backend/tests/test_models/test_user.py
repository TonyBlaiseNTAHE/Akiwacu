 #!usr/bin/python3

"""
test_user module
"""

from unittest import TestCase
from ...app import app, db
from models.subscription import Subscription
from models.user import User
from datetime import datetime



class TestUser(TestCase):
    """user test class"""
    def setUp(self):
        """ initialize database"""
        self.app_context = app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        """clean up database"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_user_subscription_relationship(self):
        """create a user"""
        user = User(username='test_user', email='test@example.com', password='123tony')
        db.session.add(user)
        db.session.commit()
    
        subscription = Subscription(start_date=datetime.now(), end_date=datetime.now(), user_id=user.id)
        db.session.add(subscription)
        db.session.commit()
        
        
        user_from_db = User.query.filter_by(username='test_user').first()
        
        self.assertIsNotNone(user_from_db.subscription)
