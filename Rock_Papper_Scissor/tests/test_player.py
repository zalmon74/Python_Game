import unittest
from pathlib import Path 
from sys import path
from shutil import copyfile
from json import dump, load

import constants_test_module as c

path.insert(0, c.PATH_MODULE_ROCK_PAPPER_SCISSOR)
from Rock_Papper_Scissor import Player
from Rock_Papper_Scissor import GlobalConstants

class TestCasePlayer(unittest.TestCase):
  """
  Тесты для класса Player
  """

  def setUp(self):
    self.name_player = "Test"
    self.path_test_file = "./test.json"
    self.obj_path_file = Path(self.path_test_file)
    self.player = Player.Player(self.name_player)
    self.count_wins  = 1
    self.count_loses = 2
    self.count_draws = 3
    for _ in range(self.count_wins):
      self.player.IncrementWins()
    for _ in range(self.count_loses):
      self.player.IncrementLoses()
    for _ in range(self.count_draws):
      self.player.IncrementDraws()

  # Проверки для статических методов
  def test_empty_file_for_save(self):
    """
    Проверка для static private метода, которвый проверят файл на пустоту.
    Если файл пустой возвращает True, иначе возвращает False.
    """
    # Открываем файл для того, чтобы отчистить его или создать, если не сущ.
    with open(self.path_test_file, "w", encoding="utf-8"):
      pass
    # Проверяем на пустоту файл
    f_empty_file = self.player._Player__EmptyFileForSaveResult(self.path_test_file)
    self.assertTrue(f_empty_file)
    # Записываем в файл какую либо информацию и проверяем, что теперь он
    # не пустой
    with open(self.path_test_file, "w", encoding="utf-8") as file:
      file.write("Test!")
    f_empty_file = self.player._Player__EmptyFileForSaveResult(self.path_test_file)
    self.assertFalse(f_empty_file)
    # После теста удаляем существующий файл
    self.obj_path_file.unlink()
    # Проверяем, возникает исключение при вызове метода без наличия файла
    self.assertRaises(FileNotFoundError, self.player._Player__EmptyFileForSaveResult
                     ,self.path_test_file)
  
  def test_create_empty_file(self):
    """
    Проверка для static private метода, который создает пустой файл по указанному
    пути.
    """
    # При помощи уже проверренного метода проверки размера файла проверяем
    # наличие файла, если файл имеется, удаляем его
    f_avail_file = self.obj_path_file.exists()
    if (f_avail_file):
      self.obj_path_file.unlink()
    self.player._Player__CreateEmptyFileForSaveResult(self.path_test_file)
    # Проверяем наличие файла
    f_avail_file = self.obj_path_file.exists()
    self.assertTrue(f_avail_file)
    # Проверяем, чтобы файл был пустым при помощи уже проверенного метода,
    # который находится в классе Player
    f_empty_file = self.player._Player__EmptyFileForSaveResult(self.path_test_file)
    self.assertTrue(f_empty_file)
    # После теста удаляем созданный файл
    self.obj_path_file.unlink()

  # Тестирование приватных методов
  def test_fromation_dic_result(self):
    """
    Тестирование метода формирования словаря с результатами игрока для записи
    в файл.
    """
    # По умолчанию кол-во побед/поражений/ничьих равняются 0
    result = 0
    # Формируем словрь с результатами
    result_dic = Player.Player(self.name_player)._Player__FormationDicForSaveInFile()
    # Выбираем результаты игрока
    result_player = result_dic[self.name_player]
    # Проверяем результаты
    self.assertEqual(len(result_dic), 1)
    self.assertEqual(result_player[GlobalConstants.STR_COUNT_WINS_GAME] , result)
    self.assertEqual(result_player[GlobalConstants.STR_COUNT_LOSES_GAME], result)
    self.assertEqual(result_player[GlobalConstants.STR_COUNT_DRAWS_GAME], result)
    # Формируем словрь с результатами
    result_dic = self.player._Player__FormationDicForSaveInFile()
    # Выбираем результаты игрока
    result_player = result_dic[self.name_player]
    # Проверяем результаты
    self.assertEqual(len(result_dic), 1)
    self.assertEqual(result_player[GlobalConstants.STR_COUNT_WINS_GAME] , self.count_wins)
    self.assertEqual(result_player[GlobalConstants.STR_COUNT_LOSES_GAME], self.count_loses)
    self.assertEqual(result_player[GlobalConstants.STR_COUNT_DRAWS_GAME], self.count_draws)
  
  def test_read_result_file_player(self):
    """
    Тестирование метода чтения файла с результатами игрока.
    """
    path_file = GlobalConstants.PATH_RESULT_PLAYER_FILE+GlobalConstants.NAME_RESULT_PLAYER_FILE
    path_copy_file = path_file + "_copy"
    # Формируем объект с файлом
    test_file = Path(path_file)
    # Проверяем наличие файла, если присутствует, то делаем его копию с другим
    # именем, чтобы не потерять содержимое данного файла, т. к. там могут
    # содержаться данные какого либо игрока
    f_avail_file = test_file.exists()
    if (f_avail_file):
      copyfile(path_file, path_copy_file)
    # Отчищаем или создаем файл
    with open(path_file, "w", encoding="utf-8"):
      pass
    # Записываем туда информаци структуированную опред. образом, чтобы
    # Она походила на результаты игрока
    result_dic = {GlobalConstants.STR_COUNT_WINS_GAME  : self.count_wins,
                  GlobalConstants.STR_COUNT_LOSES_GAME : self.count_loses,
                  GlobalConstants.STR_COUNT_DRAWS_GAME : self.count_draws}
    dic_save = {self.name_player : result_dic}
    with open(path_file, "w", encoding="utf-8") as file:
      dump(dic_save, file, indent=2)
    # С помощью Функции, которая имеется в классе Player считываем, сформированный
    # файл
    dic_result = self.player._Player__ReadResultFilePlayer()
    # Проверяем совпадения считанного и записанного словарей
    self.assertDictEqual(dic_result, dic_save)
    # Удаляем файл, с которым производился тест
    test_file.unlink()
    # Проверяем реакцию метода, если файл будет отсутсвовать. Метод должен
    # вернуть пустой словарь
    dic_result = self.player._Player__ReadResultFilePlayer()
    self.assertDictEqual(dic_result, {})
    # Возвращаем скопированный файл
    copy_file = Path(path_copy_file)
    f_avail_file = copy_file.exists()
    if (f_avail_file):
      copyfile(path_copy_file, path_file)
      copy_file.unlink() # Удаляем скопированный файл

  def test_save_result_to_file(self):
    """
    Тестирование метода записи информации об игроке в файл.
    """
    path_file = GlobalConstants.PATH_RESULT_PLAYER_FILE+GlobalConstants.NAME_RESULT_PLAYER_FILE
    path_copy_file = path_file + "_copy"
    # Формируем объект с файлом
    test_file = Path(path_file)
    # Проверяем наличие файла, если присутствует, то делаем его копию с другим
    # именем, чтобы не потерять содержимое данного файла, т. к. там могут
    # содержаться данные какого либо игрока
    f_avail_file = test_file.exists()
    if (f_avail_file):
      copyfile(path_file, path_copy_file)
    # Отчищаем или создаем файл
    with open(path_file, "w", encoding="utf-8"):
      pass
    # Сохраняем результаты в файл
    self.player.SaveResultToFile()
    # Считываем данные с файла
    with open(path_file, "r", encoding="utf-8") as file:
      dic_result = load(file)
    # Формируем словарь для проверки
    dic_res_player_test = {GlobalConstants.STR_COUNT_WINS_GAME  : self.count_wins,
                           GlobalConstants.STR_COUNT_LOSES_GAME : self.count_loses,
                           GlobalConstants.STR_COUNT_DRAWS_GAME : self.count_draws}
    dic_test = {self.name_player : dic_res_player_test}
    # Проверяем соот. файлов
    self.assertDictEqual(dic_result, dic_test)
    # Удаляем файл, с которым производился тест
    test_file.unlink()
    # Возвращаем скопированный файл
    copy_file = Path(path_copy_file)
    f_avail_file = copy_file.exists()
    if (f_avail_file):
      copyfile(path_copy_file, path_file)
      copy_file.unlink() # Удаляем скопированный файл

  # Проверка Геттеров

  def test_get_name(self):
    """
    Тестирование геттера получения имени игрока
    """
    result = self.player.GetName()
    self.assertEqual(result, self.name_player)
  
  def test_get_wins(self):
    """
    Тестирование геттера получения количества побед игрока
    """
    result = self.player.GetWins()
    self.assertEqual(result, self.count_wins)

  def test_get_loses(self):
    """
    Тестирование геттера получения количества проигрышей игрока
    """
    result = self.player.GetLoses()
    self.assertEqual(result, self.count_loses) 

  def test_get_draws(self):
    """
    Тестирование геттера получения количества ничьих игрока
    """
    result = self.player.GetDraws()
    self.assertEqual(result, self.count_draws) 
  
  def test_get_draws(self):
    """
    Тестирование геттера получения побед в процентном соот.
    """
    result = Player.Player(self.name_player).GetWinningPercentage()
    self.assertEqual(result, 0)
    test_win = self.count_wins/(self.count_wins+self.count_loses+self.count_draws)*100
    result = self.player.GetWinningPercentage()
    self.assertEqual(result, test_win)

  def test_get_count_games(self):
    """
    Тестирования геттера получения кол-ва партий, сыгранных данным игроком
    """
    count_games = self.count_wins+self.count_loses+self.count_draws
    result = self.player.GetCountGames()
    self.assertEqual(result, count_games)

  # Методы инкрементирующие поля

  def test_incr_wins(self):
    """
    Тестирование метода, который инкрементирует поля с выигрышными партиями
    """
    last = self.player._Player__count_win
    self.player.IncrementWins()
    cur = self.player._Player__count_win
    self.assertNotEqual(last, cur)
    self.assertEqual(cur, last+1)
  
  def test_incr_loses(self):
    """
    Тестирование метода, который инкрементирует поля с проигрышными партиями
    """
    last = self.player._Player__count_lose
    self.player.IncrementLoses()
    cur = self.player._Player__count_lose
    self.assertNotEqual(last, cur)
    self.assertEqual(cur, last+1)

  def test_incr_draws(self):
    """
    Тестирование метода, который инкрементирует поля партиями в ничью
    """
    last = self.player._Player__count_draw
    self.player.IncrementDraws()
    cur = self.player._Player__count_draw
    self.assertNotEqual(last, cur)
    self.assertEqual(cur, last+1)
    

if (__name__ == "__main__"):
  unittest.main()
  