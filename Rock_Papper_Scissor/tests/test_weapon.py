import unittest

import constants_test_module as c

from sys import path
path.insert(0, c.PATH_MODULE_ROCK_PAPPER_SCISSOR)
from Rock_Papper_Scissor import Weapon

class TestCaseWeapon(unittest.TestCase):
  """
  Класс для тестирования класса с оружием (Weapon) для игра в 
  камень-ножницы-бумага.
  У класса с оружием один метод получения значения, а остальные методы - 
  перегруженные операторы сравнения.
  """

  def setUp(self):
    """
    Метод для формирования начальных условий
    """
    # Формируем 2 класса с оружием с различными значениями
    self.val_weap_0 = 0
    self.val_weap_1 = 2
    self.obj_weap_0 = Weapon.Weapon(self.val_weap_0)
    self.obj_weap_1 = Weapon.Weapon(self.val_weap_1)
  
  def test_get_val(self):
    """
    Тестирование метода получения значения
    """
    self.assertEqual(self.obj_weap_0.GetNum(), self.val_weap_0)
    self.assertEqual(self.obj_weap_1.GetNum(), self.val_weap_1)
  
  def test_eq(self):
    """
    Тестирование перегруженного оператора ==
    """
    RESULT_1 = (self.val_weap_0 == self.val_weap_1)
    RESULT_2 = False # Сравнение с None
    self.assertEqual((self.obj_weap_0 == self.obj_weap_1), RESULT_1)
    self.assertEqual((self.obj_weap_0 == None), RESULT_2)
  
  def test_gt(self):
    """
    Тестирование перегруженного оператора >
    """
    RESULT_1 = (self.val_weap_0 > self.val_weap_1)
    RESULT_2 = False # Сравнение с None
    self.assertEqual((self.obj_weap_0 > self.obj_weap_1), RESULT_1)
    self.assertEqual((self.obj_weap_0 > None), RESULT_2)

  def test_lt(self):
    """
    Тестирование перегруженного оператора <
    """
    RESULT_1 = (self.val_weap_0 < self.val_weap_1)
    RESULT_2 = False # Сравнение с None
    self.assertEqual((self.obj_weap_0 < self.obj_weap_1), RESULT_1)
    self.assertEqual((self.obj_weap_0 < None), RESULT_2)

if (__name__ == "__main__"):
  unittest.main()