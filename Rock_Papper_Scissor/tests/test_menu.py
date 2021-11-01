import unittest
from sys import path

import constants_test_module as c

path.insert(0, c.PATH_MODULE_ROCK_PAPPER_SCISSOR)
from Rock_Papper_Scissor import Menu

class TestCaseMenu(unittest.TestCase):
  """
  Тестирование класса с меню
  """
  def setUp(self):
    str_0 = "Test other info!"
    str_1 = "Test_1"
    str_2 = "Test_2"
    data = [11, 22]
    self.list_all_strings = [str_1, str_2]
    self.other_info = str_0
    self.list_data = data
    self.menu = Menu.Menu(self.list_all_strings, self.list_data, self.other_info)

  def test_text_menu_other_info(self):
    """
    Тестирование выводимой информации на экран из меню с дополнительной
    инормацией
    """
    # Формируем последовательность значений, которые должно хранить меню
    nums_menu = list(range(1, len(self.list_all_strings)))
    nums_menu = [*nums_menu, 0]
    # Формируем строку, которая хранит в себе сообщение, которое должно
    # выводить меню
    text_print_menu = self.other_info + "\n"
    ind_num = 0
    for text_menu in self.list_all_strings:
      # Формирование строки вывода на экран
      text_print_menu += f"{nums_menu[ind_num]}. {text_menu}\n"
      ind_num += 1
    # Получаем значение, которое хранится в объекте
    result = self.menu._Menu__text_menu
    # Сравниваем значения
    self.assertEqual(text_print_menu, result)

  def test_text_menu(self):
    """
    Тестирование выводимой информации на экран из меню без дополнительной инфор.
    """
    # Формируем последовательность значений, которые должно хранить меню
    nums_menu = list(range(1, len(self.list_all_strings)))
    nums_menu = [*nums_menu, 0]
    # Формируем строку, которая хранит в себе сообщение, которое должно
    # выводить меню
    text_print_menu = ""
    ind_num = 0
    for text_menu in self.list_all_strings:
      # Формирование строки вывода на экран
      text_print_menu += f"{nums_menu[ind_num]}. {text_menu}\n"
      ind_num += 1
    # Получаем значение, которое хранится в объекте
    self.menu = Menu.Menu(self.list_all_strings, self.list_data)
    result = self.menu._Menu__text_menu
    # Сравниваем значения
    self.assertEqual(text_print_menu, result)

  def test_choice_player(self):
    """
    Тестирование метода выбора игрока. Что метод возвращает правильную информацию
    """
    # В списке, всего два пункта меню, и мы выбрали второй.
    # В меню он находится под номером 0
    ind_choice_data = 1
    # Формируем список чисел, которые видет пользователь
    nums_menu = list(range(1, len(self.list_all_strings)))
    nums_menu = [*nums_menu, 0]
    # Выбор пользователя
    choice = self.list_data[ind_choice_data] 
    result = self.menu.ChoicePlayer(nums_menu[ind_choice_data])
    # Проверяем соот.
    self.assertEqual(choice, result)
    # Проверяем случай, когда в меню не было такой цифры, метод должен
    # вернуть None
    result = self.menu.ChoicePlayer(999999999999999)
    self.assertIsNone(result)

if (__name__ == "__main__"):
  unittest.main()
