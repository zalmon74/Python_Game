from os import system

from SingletonDecorator import singleton
import GlobalConstants

@singleton
class MainMenu():
  """
  Класс, описывающий главный меню игры

  Поля класса:
    # text_menu - Текст, который выводится на экран при вызове соот. метода
    # dic_menu  - Сопоставление поряд. номера и ид. Для выборов от пользователя
  """

  def __init__(self):
    
    # Тексты к соот. пунктам меню
    str_1 = "Начать игру против компьютера"
    str_2 = "Выйти из игры"
    all_str_list = [str_1, str_2]

    # Формируем лист с необходимыми глобальными констанатми
    nums = list(range(0, len(all_str_list)+1))
    data = [GlobalConstants.START_GAME, GlobalConstants.EXIT_GAME]

    self.__dic_menu = {}
    self.__text_menu = ""

    ind_num = 0
    for text_str in all_str_list:
      # Формирование строки вывода на экран
      self.__text_menu += f"{nums[ind_num]}. {text_str}\n"
      # Формирование слорвая
      self.__dic_menu[ind_num] = data[ind_num]
      ind_num += 1

  # Методы

  def PrintMenu(self):
    """
    Метод получения поля с выводом текста на экран 
    """
    # Очищаем экран перед выводом меню
    system("cls || clear")
    print(self.__text_menu)
  
  def ChoicePlayer(self, num: int):
    """
    Данный метод проверяет выбор игрока. Если выбор игрока был произведен не
    правильно (не из меню), то метод вернет None, иначе соот объект.

    Вх. параметры:
      # num - Выбор пользователя

    Вых. параметры:
      # output - START_GAME = Начать игру
               , EXIT_GAME  = Выйти с игры
    """
    output = self.__dic_menu.get(num)
    return output

@singleton
class ChoiceMenu():
  """
  Данный класс предоставляет меню выбора оружия (камень, или ножницы, или 
  бумага)

  Поля класса:
    # text_menu - Текст, который выводится на экран при вызове соот. метода
    # dic_menu  - Сопоставление поряд. номера и ид. Для выборов от пользователя
  """

  def __init__(self):
    """
    Конструктор класса
    """
    # Тексты к соот. пунктам меню
    str_0 = "Выберите один из видов оружия: "
    str_1 = "Камень"
    str_2 = "Ножницы"
    str_3 = "Бумага"
    all_str_list = [str_1, str_2, str_3]

    # Формируем лист с необходимыми глобальными констанатми
    nums = list(range(0, len(all_str_list)+1))
    data = [GlobalConstants.ROCK_WEAP, GlobalConstants.SCISSOR_WEAP
           ,GlobalConstants.PAPER_WEAP]

    self.__dic_menu = {}
    self.__text_menu = str_0 + "\n"

    ind_num = 0
    for text_str in all_str_list:
      # Формирование строки вывода на экран
      self.__text_menu += f"{nums[ind_num]}. {text_str}\n"
      # Формирование слорвая
      self.__dic_menu[ind_num] = data[ind_num]
      ind_num += 1

  # Методы

  def PrintMenu(self):
    """
    Метод получения поля с выводом текста на экран 
    """
    # Очищаем экран перед выводом меню
    system("cls || clear")
    print(self.__text_menu)

  def ChoicePlayer(self, num: int):
    """
    Данный метод проверяет выбор игрока. Если выбор игрока был произведен не
    правильно (не из меню), то метод вернет None.

    Вх. параметры:
      # num - Выбор пользователя

    Вых. параметры:
      # output - None         = если пользователь ввел не правильное значение
                 ROCK_WEAP    = если пользователь выборал в виде оружия камень
                 SCISSOR_WEAP = если пользователь выборал в виде оружия ножницы
                 PAPER_WEAP   = если пользователь выборал в виде оружия бумагу
    """
    # Если метод "get" вернул None, то пользователь ввел не правильно
    output = self.__dic_menu.get(num)
    return output

@singleton
class EndMenu():
  """
  Данный класс предоставляет меню выбора после партии в игре 
  (продолжить играть или закончить)

  Поля класса:
    # text_menu - Текст, который выводится на экран при вызове соот. метода
    # dic_menu  - Сопоставление поряд. номера и ид. Для выборов от пользователя
  """

  def __init__(self):
    """
    Конструктор класса
    """
    # Тексты к соот. пунктам меню
    str_0 = "Выберите один из пунктов ниже: "
    str_1 = "Продолжить игру (начать следующую партию)"
    str_2 = "Закончить игру (выйти в главное меню)"
    all_str_list = [str_1, str_2]

    # Формируем лист с необходимыми глобальными констанатми
    nums = list(range(0, len(all_str_list)+1))
    data = [GlobalConstants.CONTINUE_GAME, GlobalConstants.END_GAME]

    self.__dic_menu = {}
    self.__text_menu = str_0 + "\n"

    ind_num = 0
    for text_str in all_str_list:
      # Формирование строки вывода на экран
      self.__text_menu += f"{nums[ind_num]}. {text_str}\n"
      # Формирование слорвая
      self.__dic_menu[ind_num] = data[ind_num]
      ind_num += 1

  # Методы

  def PrintMenu(self):
    """
    Метод получения поля с выводом текста на экран 
    """
    print(self.__text_menu)

  def ChoicePlayer(self, num: int):
    """
    Данный метод проверяет выбор игрока. Если выбор игрока был произведен не
    правильно (не из меню), то метод вернет None.

    Вх. параметры:
      # num - Выбор пользователя

    Вых. параметры:
      # output - None           = если пользователь ввел не правильное значение
                 CONTUNIUE_GAME = если пользователь выборал полжить игру
                 END_GAME       = если пользователь выборал выйти в глав. меню
    """
    # Если метод "get" вернул None, то пользователь ввел не правильно
    output = self.__dic_menu.get(num)
    return output