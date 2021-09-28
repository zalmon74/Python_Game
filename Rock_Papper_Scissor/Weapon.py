class Weapon():
  """
  Данный класс описывает оружие, которое возможно использовать в игре.
  (Камень-Ножницы-Бумага)

  Поля класса:
    # num - внутреннее значение класса для идентификации оружия
  """

  def __init__(self, num):
    """
    Конструктор класса
    Вх. аргументы:
      # num - внутреннее значение класса для идентификации оружия
    """
    self.__num = num

  def GetNum(self):
    """
    Геттер для просмотра значения внутри класса (Просмотр ИД объекта)
    """
    return self.__num

  def __eq__(self, other):
    """
    Перегрузка оператора ==
    """
    output = False
    if (other == None):
      output = False    
    elif (self.__num == other.GetNum()):
      output = True
    return output

  def __gt__(self, other):
    """
    Перегрузка оператора >
    """
    output = False
    if (self.__num > other.GetNum()):
      output = True
    return output

  def __lt__(self, other):
    """
    Перегрузка оператора <
    """
    output = False
    if (self.__num < other.GetNum()):
      output = True
    return output