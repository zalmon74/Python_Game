from Rock_Papper_Scissor import GlobalConstants

class Menu():
  """
  Данный класс описывает меню.
  
  Поля класса:
    # text_menu - Текст, который выводится на экран при вызове соот. метода
    # dic_menu  - Сопоставление поряд. номера и ид. Для выборов от пользователя
  """
  def __init__(self, all_str_list: list, data: list, other_info = ""):
    """
    Конструктор класса.

    Вх. аргументы:
      # all_str_list - список строк, который соот. пунктам к меню
      # data - список с константами, которые соот. определенному поведению
               игры, после выбора соот. пунка из меню
    """
    # Проверка на соот. размерностей
    if (len(all_str_list) != len(data)):
      raise Exception(f"Размер списка со строками ({len(all_str_list)}) не равен\
                        размеру списка с данными ({len(data)})") 
    # Формируем лист с перечислением
    nums = list(range(1, len(all_str_list)))
    nums = [*nums, 0]
    self.__dic_menu = {}
    self.__text_menu = "" if (len(other_info) == 0) else (other_info+"\n")
    ind_num = 0
    for text_str in all_str_list:
      # Формирование строки вывода на экран
      self.__text_menu += f"{nums[ind_num]}. {text_str}\n"
      # Формирование слорвая
      self.__dic_menu[nums[ind_num]] = data[ind_num]
      ind_num += 1
  
  # Методы
  
  def PrintMenu(self):
    """
    Метод вывода текста меню на экран 
    """
    print(self.__text_menu)

  def ChoicePlayer(self, num: int):
    """
    Данный метод проверяет выбор игрока. Если выбор игрока был произведен не
    правильно (не из меню), то метод вернет None, иначе соот объект.

    Вх. параметры:
      # num - Выбор пользователя
    """
    output = self.__dic_menu.get(num)
    return output

def formation_main_menu():
  """
  Функция создания объекта с главным меню

  Вых. аргументы:
    # main_menu - сформированный объект типа Menu
  """
  # Тексты к соот. пунктам меню
  str_1 = "Начать игру против компьютера"
  str_2 = "Выйти из игры"
  all_str_list = [str_1, str_2]
  # Формируем лист с необходимыми глобальными констанатми
  data = [GlobalConstants.START_GAME, GlobalConstants.EXIT_GAME]
  return Menu(all_str_list, data)

def formation_choice_menu():
  """
  Функция создания объекта с меню выбором оружения (камень, или ножницы, или 
  бумага)

  Вых. аргументы:
    # choice_menu - сформированный объект типа Menu
  """
  # Тексты к соот. пунктам меню
  str_0 = "Выберите один из видов оружия: "
  str_1 = "Камень"
  str_2 = "Ножницы"
  str_3 = "Бумага"
  all_str_list = [str_1, str_2, str_3]
  # Формируем лист с необходимыми глобальными констанатми
  data = [GlobalConstants.ROCK_WEAP, GlobalConstants.SCISSOR_WEAP
          ,GlobalConstants.PAPER_WEAP]
  return Menu(all_str_list, data, str_0) 

def formation_end_menu():
  """
  Функция создания объекта с меню выбора после партии в игре 

  Вых. аргументы:
    # end_menu - сформированный объект типа Menu
  """

  # Тексты к соот. пунктам меню
  str_0 = "Выберите один из пунктов ниже: "
  str_1 = "Продолжить игру (начать следующую партию)"
  str_2 = "Просмотр результатов"
  str_3 = "Закончить игру (выйти в главное меню)"
  all_str_list = [str_1, str_2, str_3]
  # Формируем лист с необходимыми глобальными констанатми
  data = [GlobalConstants.CONTINUE_GAME, GlobalConstants.RESULT_PLAYER
          ,GlobalConstants.END_GAME]
  return Menu(all_str_list, data, str_0) 

def formation_result_menu():
  """
  Функция создания объекта с меню выбора просмотра результатов игрока

  Вых. аргументы:
    # result_menu - сформированный объект типа Menu
  """
  # Тексты к соот. пунктам меню
  str_0 = "Выберите один из пунктов ниже: "
  str_1 = "Посмотреть количество побед"
  str_2 = "Посмотреть процент побед"
  str_3 = "Посмотреть количество поражений"
  str_4 = "Посмотреть количество ничьих"
  str_5 = "Продолжить игру"
  str_6 = "Закончить игру (выйти в главное меню)"
  all_str_list = [str_1, str_2, str_3, str_4, str_5, str_6]

  # Формируем лист с необходимыми глобальными констанатми
  data = [GlobalConstants.CHECK_COUNT_WINS , GlobalConstants.CHECK_COUNT_PROC_WINS
          ,GlobalConstants.CHECK_COUNT_LOSES, GlobalConstants.CHECK_COUNT_DRAW
          ,GlobalConstants.CONTINUE_GAME, GlobalConstants.END_GAME]
  return Menu(all_str_list, data, str_0) 