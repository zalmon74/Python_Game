class Player():
  """
  Класс, описывающий игрока (его параметры, возможности и тп. для игры в
  камень-ножницы-бумага)

  Поля класса:
    # name - Имя игрока
    # count_win  - Кол-во побед в игре
    # count_lose - Кол-во поражений в игре 
  """

  def __init__(self, name: str):
    """
    Конструктор класса игрока.

    Вх. параметры:
      # name - Имя игрока
    """
    self.__name = name
    self.__count_win  = 0 
    self.__count_lose = 0
    self.__count_draw = 0

  # Геттеры

  def GetName(self):
    """
    Метод получения имени игрока
    """
    return self.__name

  def GetWins(self):
    """
    Метод получения количества выйгранных партий пользователя
    """
    return self.__count_win

  def GetLoses(self):
    """
    Метод получения количества проигрышных партий пользователя
    """
    return self.__count_lose

  def GetDraws(self):
    """
    Метод получения количества партий, которые были сыграны в ничью
    """
    return self.__count_draw
  
  def GetWinningPercentage(self):
    """
    Метод получения количества побед в процентном соотношении
    """

    output = 0
    # Если делить без условия, то может возникнуть ситуация деления 0 на 0
    if ((self.__count_lose != 0)  or 
        (self.__count_win  != 0)  or 
        (self.__count_draw != 0)):

      output = self.__count_win/(self.__count_lose 
                            + self.__count_win
                            + self.__count_draw
                            )*100
    return output

  # Методы инкрементирующие поля
  
  def IncrementWins(self):
    """
    Метод инкрементирующий поле с количеством выйгрышных партий у пользователя
    """  
    self.__count_win += 1

  def IncrementLoses(self):
    """
    Метод инкрементирующий поле с количеством проигрышных партий у пользователя
    """  
    self.__count_lose += 1

  def IncrementDraws(self):
    """
    Метод инкрементирующий поле с количеством ничьих у пользователя
    """  
    self.__count_draw += 1
