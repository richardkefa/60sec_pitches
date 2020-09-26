import unittest
from app.models import Pitch,User

class TestUser(unittest.TestCase):
  def setUp(self):
    self.new_pitch = Pitch(title='product selling',
                           pitch='you need to be presentable to sell products',
                           category='product pitch',
                           )
    
  def tearDown(self):
      Pitch.query.delete()
      User.query.delete()
      
  def test_check_instance_variable(self):
    self.assertEqual(self.new_pitch.title,'product selling')
    self.assertEqual(self.new_pitch.pitch,'you need to be presentable to sell products')
    self.assertEqual(self.new_pitch.category,'product pitch')

  def test_save_pitch(self):
    self.new_pitch.save_pitch()
    self.assertTrue(len(Pitch.query.all())>0)
    
  def test_get_pitch(self):
    self.new_pitch.save_pitch()
    get_pitch = Pitch.query.first()
    self.assertTrue(len(get_pitch) == 1)