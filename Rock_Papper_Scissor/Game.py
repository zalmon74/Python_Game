from random import choice, randint
from os import system
from time import sleep
import socket

import Menu
import GlobalConstants
from Player import Player
from Rock_Papper_Scissor.Weapon import Weapon
from SingletonDecorator import singleton

@singleton
class Game():
  """
  В данном классе будет описано взаимодействие различных компонентов между собой
  для создания игры (иначе говоря сама игра)

  Поля класса:
    # cur_player  - объект с текущим игроком
    # main_menu   - объект с главным меню игры
    # end_menu    - объект с меню после партии
    # choice_menu - объект с меню для выбора оружия
    # result_menu - объект с меню для просмотра кол-ва побед/поражений/ничьих игрока
  """

  # Приватные методы
  @staticmethod
  def __InputValue(text = ""):
    """
    Метод, который ожидает, что пользователь введет число, если пользователь
    ввел не число, он перезапрашивает ввод, пока пользователь не введет число.
    """
    f_right = False
    while (not f_right):
      try:
        value = int(input(text))
      except ValueError:
        print("Вы ввели не число. Попробуйте еще раз!\n")
      else:
        f_right = True
    return value


  def __ChoicePlayer(self, menu):
    """
    Метод, который печает соот. меню игры и выбирает из него пункт

    Вх. аргументы: 
      # menu - Меню, в котором находится пользователь

    Вых. аргументы:
      # output - Выбор игрока или None (если выбор был не верен)
    """
    menu.PrintMenu()
    in_choice_menu_player = self.__InputValue()
    # Очищаем экран для того, чтобы следующее меню было выведено на пустой экран
    system("cls || clear")
    choice_menu_player = menu.ChoicePlayer(in_choice_menu_player)
    return choice_menu_player

  def __ChoicePlayerInMenu(self, menu):
    """
    Метод, который требует от пользователя ввести правильное значение
    из меню, если оно будет введено неверно, то у пользователя будет
    запрошено значение еще раз.

    Вх. аргументы: 
      # menu - Меню, в котором находится пользователь

    Вых. аргументы:
      # output - Выбор игрока 
    """
    # Флаг, который установлен, пока пользователь не введет
    # верный вариант
    f_menu = True
    while (f_menu): 
      # Вызываем главеное меню игры и ждем верный ответ от пользователя
      choice_menu_player = self.__ChoicePlayer(menu)
      # Если выбранный объект пользователем равен None, то он ввел значение
      # не из меню, поэтому необходимо снова запросить правильный ответ
      if (choice_menu_player != None):
        f_menu = False
      else:
        print("Вы ввели значение не из меню. Проверьте правильность ввода!\n")
    return choice_menu_player  

  def __OpponentChoice(self):
    """
    Метод, который описывает поведение противника (его выбор)

    Вых. аргументы:
      # weap - оружие, которе выбрал противник
    """
    # Противник выбирает (камень-ножницы-бумага) случайным образом
    num = randint(0,2)
    weap = self.__choice_menu.ChoicePlayer(num)
    return weap

  def __ComparisonChoices(self, choice):
    """
    Метод сопоставления объекта и соот. строки (названия данного объекта)

    Вх. аргументы: 
      # choice - объект, который необходимо сопоставить

    Вых. аргументы:
      # output_str - строка, которая содержит в себе название объекта
    """
    output_str = None
    if (choice == GlobalConstants.ROCK_WEAP):
      output_str = "Камень"
    elif (choice == GlobalConstants.SCISSOR_WEAP):
      output_str = "Ножницы"
    elif (choice == GlobalConstants.PAPER_WEAP):
      output_str = "Бумага"
    return output_str

  def __PrintChoicePlayers(self, choice_player, choice_opponent):
    """
    Метод печати на экран выборы игроков

    Вх. аргументы:
      # choice_player   - Выбор игрока
      # choice_opponent - Выбор оппонента
    """
    name_weap_player   = self.__ComparisonChoices(choice_player)
    name_weap_opponent = self.__ComparisonChoices(choice_opponent)
    # Очищаем экран перед выводом
    system("cls || clear")
    print(f"Игрок выбрал оружие: {name_weap_player.lower()}")
    print(f"Оппонент выбрал оружие: {name_weap_opponent.lower()}\n")

  def __DeterminWinner(self, choice_player, choice_opponent):
    """
    Метод определения победителя.

    Вх. аргументы: 
      # choice_player   - выбор оружия игрока
      # choice_opponent - выбор оружия оппонента

    Вых. аргументы:
      # output - DRAW         = Ничья
                 WIN_PLAYER   = Победил игрок
                 WIN_OPPONENT = Победил оппонент
    """

    output = None
    if (choice_player == choice_opponent):
      output = GlobalConstants.DRAW
      self.__cur_player.IncrementDraws()
    # Камень бьет Ножницы
    elif ((choice_player   == GlobalConstants.ROCK_WEAP)     and
          (choice_opponent == GlobalConstants.SCISSOR_WEAP)):
      output = GlobalConstants.WIN_PLAYER
      self.__cur_player.IncrementWins()
    # Ножницы бьют бумагу
    elif ((choice_player   == GlobalConstants.SCISSOR_WEAP) and
          (choice_opponent == GlobalConstants.PAPER_WEAP)):
      output = GlobalConstants.WIN_PLAYER
      self.__cur_player.IncrementWins()
    # Бумага бьет камень
    elif ((choice_player   == GlobalConstants.PAPER_WEAP) and
          (choice_opponent == GlobalConstants.ROCK_WEAP)):
      output = GlobalConstants.WIN_PLAYER
      self.__cur_player.IncrementWins()
    else:
      output = GlobalConstants.WIN_OPPONENT
      self.__cur_player.IncrementLoses()
    return output

  def __PrintWinner(self, result):
    """
    Метод вывода на экран победителя

    Вх. аргументы:
      # result - Результат партии
    """ 
    if (result == GlobalConstants.DRAW):
      print("Ничья!\n")
    elif (result == GlobalConstants.WIN_PLAYER):
      print(f"Вы победили!\n")
    elif (result == GlobalConstants.WIN_OPPONENT):
      print("Вы проиграли!\n")

  def __PlayGameWithBot(self):
    """
    Метод, который описывает саму игру
    """
    print(f"{self.__cur_player.GetName()} выберите пожалуйста оружие.\n")
    # Игрок выбрал свое оружие
    choice_player = self.__ChoicePlayerInMenu(self.__choice_menu)
    # Противник выбирает свое оружие
    choice_opponent = self.__OpponentChoice()
    # Вывод на экран выборы игрока и оппонента (бота)
    self.__PrintChoicePlayers(choice_player, choice_opponent)
    # Определение победителя
    result = self.__DeterminWinner(choice_player, choice_opponent)
    self.__PrintWinner(result)

  def __PlayLocalGame(self, obj_socket: socket.socket):
    """
    Метод, который описывает саму игру
    """
    print(f"{self.__cur_player.GetName()} выберите пожалуйста оружие.\n")
    # Игрок выбрал свое оружие
    choice_player = self.__ChoicePlayerInMenu(self.__choice_menu)
    choice_player = str(choice_player.GetNum()).encode()
    # Отправляем выбранное оружие второму игроку
    obj_socket.send(choice_player)
    print("\n Ожидаем выбор оружия второго игрока\n")
    # Ожидаем выбор оружия от второго игрока
    choice_opponent = obj_socket.recv(GlobalConstants.BUF_SIZE_SOCKET) 
    # Переформируем полученный ответ в объект
    choice_player = Weapon(int(choice_player.decode()))
    choice_opponent = Weapon(int(choice_opponent.decode()))
    # Вывод на экран выбора игрока и оппонента 
    self.__PrintChoicePlayers(choice_player, choice_opponent)
    # Определение победителя
    result = self.__DeterminWinner(choice_player, choice_opponent)
    self.__PrintWinner(result)

  def __PrintResultPlayer(self, choice_player):
    """
    Метод вывода на экран значение с результатами игрока 
    (кол-во побед/поражений/ничьих)

    Вх. аргументы: 
      # choice_player - Выбор игрока из меню с результатами
    """
    # Количество сыгранных игр пользователем
    count_games = self.__cur_player.GetCountGames() 
    # Строка для вывода на экран
    str = f"Вы сыграли {count_games} партий " 
    if (choice_player == GlobalConstants.CHECK_COUNT_WINS):
      res = self.__cur_player.GetWins()
      str += f"из них кол-во побед {res}."
    elif (choice_player == GlobalConstants.CHECK_COUNT_PROC_WINS):
      res = self.__cur_player.GetWinningPercentage()
      str += f"количество побед составляет {res}%."
    elif (choice_player == GlobalConstants.CHECK_COUNT_LOSES):
      res = self.__cur_player.GetLoses()
      str += f"из них кол-во поражений {res}."
    elif (choice_player == GlobalConstants.CHECK_COUNT_DRAW):
      res = self.__cur_player.GetDraws()
      str += f"из них кол-во ничьих {res}."
    print(str + "\n")

  def __ServerGamePlayer(self):
    """
    Метод, который описывает сервер в игре при локальной сети.
    """
    # Запрашиваем порт сервера
    port = self.__InputValue("Введите порт сервера: ")
    # Создаем сокет
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Устанавливаем время подключения
    server_socket.settimeout(GlobalConstants.TIMEOUT_LOCAL_GAME)
    # Связываем сокет с портом
    server_socket.bind(("", port))
    # Устанавливаем максимальное количество клиентов
    server_socket.listen(1)
    # Очищаем экран перед выводом
    system("cls || clear")
    print("Ожидаем подключение игрока\n")
    # Ожидаем подключение клиента
    try:
      connection_socket, address_client = server_socket.accept()
    except socket.timeout: # Если время подключения истекло
      print("\nВремя подключения истекло")
      sleep(2)
      # Очищаем экран
      system("cls || clear")
      server_socket.close()
      return
    # Запускаем непрерывную игру (пока пользователь не выйдет в главное меню)
    try:
      self.__PlayInfLocalGame(connection_socket)
    except ConnectionAbortedError:
      print("Второй игрок вышел из игры!")
      sleep(2)
      # Очищаем экран
      system("cls || clear")
    connection_socket.close()
    server_socket.close()
    
  def __ClientGamePlayer(self):
    """
    Метод, который описывает клиента в игре при локальной сети.
    """
    # Запрашиваем ip-сервера
    ip_server = input("Введите ip сервера: ")
    # Запрашиваем порт сервера
    port = self.__InputValue("Введите порт сервера: ")
    # Создаем сокет
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Устанавливаем время подключения
    client_socket.settimeout(GlobalConstants.TIMEOUT_LOCAL_GAME)
    # Очищаем экран перед выводом
    system("cls || clear")
    print("Ожидаем подключение к серверу\n")
    # Подключаемся к серверу
    try:
      client_socket.connect((ip_server, port))
    except socket.gaierror: # Если время подключения истекло
      print("\nТакого сервера не существует")
      sleep(2)
      # Очищаем экран
      system("cls || clear")
      client_socket.close()
      return  
    # Запускаем непрерывную игру (пока пользователь не выйдет в главное меню)
    try:
      self.__PlayInfLocalGame(client_socket)
    except ConnectionAbortedError:
      print("Второй игрок вышел из игры!")
      sleep(2)
      # Очищаем экран
      system("cls || clear")
    client_socket.close()

  def __PlayInfLocalGame(self, obj_socket: socket.socket):
    """
    Метод для непрерыввной игры по локальной сети. 
    """
    f_cont_game = True # Флаг продолжения игры
    while (f_cont_game):
      self.__PlayLocalGame(obj_socket) 
      choice_menu_player = self.__ChoicePlayerInMenu(self.__end_menu)
      # Если пользователь выбрал меню просмотр результатов, то выводим меню
      # и ждем его выброр, зависимости от выбора выводим на экран результаты
      if (choice_menu_player == GlobalConstants.RESULT_PLAYER):
        # Флаг, определяющий хочет ли пользователь находитсяв меню
        # с результатами или нет
        f_result = True 
        while (f_result):
          choice_menu_player = self.__ChoicePlayerInMenu(self.__result_menu)
          # Если пользователь выбрал продолжить игру или выйти в главное меню,
          # то заканчиваем цикл и идем в соот. с выбором пользователя
          if ((choice_menu_player == GlobalConstants.CONTINUE_GAME) or
              (choice_menu_player == GlobalConstants.END_GAME)):
            f_result = False
          else:
            # Если игрок выбрал один из пунктов печати результата, то
            # вызываем соот. метод
            self.__PrintResultPlayer(choice_menu_player)
      # Если игрок выбор выйти в главное меню, то флаг продолжения игры
      # устанавливается в False и игра выходит в главное меню
      if (choice_menu_player == GlobalConstants.END_GAME):
        f_cont_game = False
    
  # Конструкторы

  def __init__(self) :
    """
    Конструктор класса с игрой
    """
    # Очищаем экран перед запуском игры
    system("cls || clear")
    # Выводим надпись, о том что пользователь запустил игру.
    print("Вы запустили игру \"Камень-Ножницы-Бумага\"")
  
    # Получаем имя игрока и создаем соот. объект
    name = input("Представтесь: ")
    self.__cur_player = Player(name)

    # Очищаем экран, чтобы следующее меню было выведено на пустой экран
    system("cls || clear")

    # Создаем объекты меню для игры
    self.__main_menu       = Menu.formation_main_menu()
    self.__local_game_menu = Menu.formation_local_game_menu()
    self.__end_menu        = Menu.formation_end_menu()
    self.__choice_menu     = Menu.formation_choice_menu()
    self.__result_menu     = Menu.formation_result_menu()

  # Методы

  def StartGame(self):
    """
    Метод, запускающий игру
    """

    f_game = True # Флаг, что игра продолажется
    # Бесконечный цикл для того, чтобы игра не завершилась после первой партии
    while (f_game):
      
      # Вызываем главное меню игры и ждем выбор пользователя
      choice_menu_player = self.__ChoicePlayerInMenu(self.__main_menu)
            
      # После выбора игрока надо посмотреть, что он выбрал:
      # Начать играть или выйти из игры
      if (choice_menu_player == GlobalConstants.START_GAME):
        f_cont_game = True # Флаг продолжения игры
        while (f_cont_game):
          self.__PlayGameWithBot()
          choice_menu_player = self.__ChoicePlayerInMenu(self.__end_menu)
          # Если пользователь выбрал меню просмотр результатов, то выводим меню
          # и ждем его выброр, зависимости от выбора выводим на экран результаты
          if (choice_menu_player == GlobalConstants.RESULT_PLAYER):
            # Флаг, определяющий хочет ли пользователь находитсяв меню
            # с результатами или нет
            f_result = True 
            while (f_result):
              choice_menu_player = self.__ChoicePlayerInMenu(self.__result_menu)
              # Если пользователь выбрал продолжить игру или выйти в главное меню,
              # то заканчиваем цикл и идем в соот. с выбором пользователя
              if ((choice_menu_player == GlobalConstants.CONTINUE_GAME) or
                 (choice_menu_player == GlobalConstants.END_GAME)):
                f_result = False
              else:
                # Если игрок выбрал один из пунктов печати результата, то
                # вызываем соот. метод
                self.__PrintResultPlayer(choice_menu_player)
          # Если игрок выбор выйти в главное меню, то флаг продолжения игры
          # устанавливается в False и игра выходит в главное меню
          if (choice_menu_player == GlobalConstants.END_GAME):
            f_cont_game = False
      # Выбор игры по локальной сети      
      elif (choice_menu_player == GlobalConstants.START_LOCAL_GAME):
        # Ожидаем выбор игрока
        choice_menu_player = self.__ChoicePlayerInMenu(self.__local_game_menu)
        if (choice_menu_player == GlobalConstants.CREATE_LOCAL_GAME):
          self.__ServerGamePlayer()
        elif (choice_menu_player == GlobalConstants.CONNECTION_LOCAL_GAME):
          self.__ClientGamePlayer()        
      # Выбор выхода из игры
      elif (choice_menu_player == GlobalConstants.EXIT_GAME):
        f_game = False
        # Очищаем экран перед выводом
        system("cls || clear")
        str_output  = "Спасибо за игру. Ваш процент выйгрышей составил: "
        str_output += str(round(self.__cur_player.GetWinningPercentage(), GlobalConstants.PREC_DISP_RES_WINS))
        str_output += "%. Всего доброго!"
        print(str_output)
        
        # Сохраняем результаты игрока
        self.__cur_player.SaveResultToFile()


    