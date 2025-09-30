import unittest
from app.main import add

class TestApp (unittest.TestCase):
  def test_add (self):
    self.assertEqual (add(2, 3), 5)
if _name_ == "_main_":
  unittest.main()
