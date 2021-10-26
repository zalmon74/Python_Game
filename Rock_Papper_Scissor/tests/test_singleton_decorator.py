import unittest

import constants_test_module as c

from sys import path
path.insert(0, c.PATH_MODULE_ROCK_PAPPER_SCISSOR)
from Rock_Papper_Scissor import SingletonDecorator

# Создаем класс для тестирования
@SingletonDecorator.singleton
class SingletonClass():
  """
  Класс для создания объектов при тестировании декоратора
  Singleton
  """
  def __init__(self, val):
    self.val = val
  
class TestSingletonDecor(unittest.TestCase):
  """
  Тестирование декоратора SingletonDecorator
  """

  def setUp(self):
    self.val_0 = 13
    self.val_1 = 56
    self.obj_0 = SingletonClass(self.val_0)
    self.obj_1 = SingletonClass(self.val_1)

  def test_singleton(self):
    self.assertTrue(self.obj_0 is self.obj_1)
    self.assertEqual(self.obj_0.val, self.val_0)
    self.assertEqual(self.obj_1.val, self.val_0)
    
if (__name__ == "__main__"):
  unittest.main()