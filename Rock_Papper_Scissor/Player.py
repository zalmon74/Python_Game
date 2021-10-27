import json
from json.decoder import JSONDecodeError
from os import stat, path

from Rock_Papper_Scissor import GlobalConstants

class Player():
  """
  Класс, описывающий игрока (его параметры, возможности и тп. для игры в
  камень-ножницы-бумага)

  Поля класса:
    # name - Имя игрока
    # count_win  - Кол-во побед в игре
    # count_lose - Кол-во поражений в игре 
  """
  
  # Статические методы

  @staticmethod
  def __EmptyFileForSaveResult(path_file : str):
    """
    Метод проверки пустого файла для записи результатов игрока

    Вх. аргументы:
      # path_file - путь до файла

    Вых. аргументы: 
      # output = True  - если файл пустой
                 False - если файл не пустой 
    """
    output = (stat(path_file).st_size == 0)
    return output
  
  @staticmethod
  def __CreateEmptyFileForSaveResult(path_file : str):
    """
    Метод создания пустого файла для сохранение результатов текущего игрока,
    если такого файла не существует

    Вх. аргументы:
      # path_file - путь до файла
    """
    f_file_avail =  path.isfile(path_file)
    # Если файла не существует, то создаем его, иначе ничего не делаем
    if (not f_file_avail):
      with open(path_file, "w", encoding=GlobalConstants.ENCODING_FOR_FILE):
        pass



  # Приватные методы

  def __FormationDicForSaveInFile(self):
    """
    Метод формирования словаря с результатами игрока для сохранения их в файл

    Вых. аргументы:
      # result_player_dic - словарь, где ключ = имя игрока, 
      #                     а данные = его результаты
    """
    # Словарь, который хранит только результаты
    result_dic = {
                  GlobalConstants.STR_COUNT_WINS_GAME  : self.__count_win,
                  GlobalConstants.STR_COUNT_LOSES_GAME : self.__count_lose,
                  GlobalConstants.STR_COUNT_DRAWS_GAME : self.__count_draw 
                 }
    # Словарь, который хранит результаты для определенного пользователя
    result_player_dic = {self.__name : result_dic}
    return result_player_dic

  def __ReadResultFilePlayer(self):
    """
    Метод чтение файла с результатами игрока, если данный файл имеется

    Вых. аргументы:
      # result_save_to_file - результаты игроков, которые были сохранены ранее
    """
    path_file = GlobalConstants.PATH_RESULT_PLAYER_FILE + GlobalConstants.NAME_RESULT_PLAYER_FILE
    try:
      with open(path_file, "r", encoding=GlobalConstants.ENCODING_FOR_FILE) as file:
        result_save_to_file = json.load(file) 
    # Если такого файла нет, то делаем словарь пустой
    except (FileNotFoundError, JSONDecodeError): 
      result_save_to_file = {}

    return result_save_to_file

  def __init__(self, name: str):
    """
    Конструктор класса игрока.

    Вх. параметры:
      # name - Имя игрока
    """
    self.__name = name
    # Считываем с файла результаты игроков и проверяем наличие тек. игрока.
    # Если текущий игрок уже имеется в файлах, то берем результаты от туда,
    # иначе они равны 0
    result_players = self.__ReadResultFilePlayer()
    result_player = result_players.get(name)
    
    count_wins  = 0
    count_loses = 0
    count_draws = 0

    if (result_player != None):
      count_wins  = result_player[GlobalConstants.STR_COUNT_WINS_GAME]
      count_loses = result_player[GlobalConstants.STR_COUNT_LOSES_GAME]
      count_draws = result_player[GlobalConstants.STR_COUNT_DRAWS_GAME]
    
    self.__count_win  = count_wins
    self.__count_lose = count_loses
    self.__count_draw = count_draws

  # Методы

  def SaveResultToFile(self):
    """
    Метод записи результатов игрока в файл

    Вх. аргументы:
      # result_player_dic - словарь с результатами игрока, который необходимо
      #                     записать в файл
    """
    # Формируем имя файла и открываем его для добавление в него записи
    path_file = GlobalConstants.PATH_RESULT_PLAYER_FILE + GlobalConstants.NAME_RESULT_PLAYER_FILE
    # Вызываем функцию создания файла, если он не сущетствует
    self.__CreateEmptyFileForSaveResult(path_file)
    with open(path_file, "r+", encoding=GlobalConstants.ENCODING_FOR_FILE) as file:
      # Формируем словарь с результатами игрока
      result_player = self.__FormationDicForSaveInFile()
      # Вызываем функцию, которая считает из файла все данные и вернет словарь 
      result_save_to_file = self.__ReadResultFilePlayer()
      # Формируем новый словарь с результатами текущего игрока
      result_save_to_file = {**result_save_to_file, **result_player}
      # Сохраняем новые результаты в файл
      file.seek(0)
      json.dump(result_save_to_file, file, indent=2)

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
    if (self.GetCountGames() != 0):
      output = self.__count_win/(self.GetCountGames())*100
    return output

  def GetCountGames(self):
    """
    Метод подсчета количества игр, которые сыграл пользователь
    """
    return (self.__count_lose + self.__count_win + self.__count_draw)

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
