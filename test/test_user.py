import unittest
from app.models import User
from app import db

class TestUser(unittest.TestCase):
  def setUp(self):
    self.user_kefa = User(username='kefa',
                          pass_secure="1234",
                          email='richardkefa7@gmail.com',
                          bio='I am great'
                          )
    
  def tearDown(self):
    User.query.delete()
    
    
  def test_instance_variable(self):
    self.assertEqual(self.user_kefa.username,'kefa')
    self.assertEqual(self.user_kefa.email,'richardkef7@gmail.com')
    self.assertEqual(self.user_kefa.bio,'I am great')
    
  def test_passwords_setter(self):
    self.assertTrue(self.user_kefa.pass_secure is not None)
    
  def test_password_verification(self):
    self.assertTrue(self.user_kefa.verify_password('1234'))
    