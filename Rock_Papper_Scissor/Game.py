from random import randint

import Menu
import GlobalConstants
from Player import Player
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
  """

  # Приватные методы

  def __ChoicePlayer(self, menu):
    """
    Метод, который печает соот. меню игры и выбирает из него пункт

    Вх. аргументы: 
      # menu - Меню, в котором находится пользователь

    Вых. аргументы:
      # output - Выбор игрока или None (если выбор был не верен)
    """
    menu.PrintMenu()
    in_choice_menu_player = int(input())
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
        print("Вы ввели значение не из меню. Проверьте правильность ввода!")
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
    print(f"Игрок выбрал оружие: {name_weap_player.lower()}")
    print(f"Оппонент выбрал оружие: {name_weap_opponent.lower()}")

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
      print("Ничья!")
    elif (result == GlobalConstants.WIN_PLAYER):
      print(f"Победил игрок {self.__cur_player.GetName()}")
    elif (result == GlobalConstants.WIN_OPPONENT):
      print("Победил бот!")

  def __PlayGame(self):
    """
    Метод, который описывает саму игру
    """
    print(f"{self.__cur_player.GetName()} выберите пожалуйста оружие.")
    # Игрок выбрал свое оружие
    choice_player = self.__ChoicePlayerInMenu(self.__choice_menu)
    # Противник выбирает свое оружие
    choice_opponent = self.__OpponentChoice()
    # Вывод на экран выборы игрока и оппонента (бота)
    self.__PrintChoicePlayers(choice_player, choice_opponent)
    # Определение победителя
    result = self.__DeterminWinner(choice_player, choice_opponent)
    self.__PrintWinner(result)
    
  # Конструкторы

  def __init__(self) :
    """
    Конструктор класса с игрой
    """
    # Выводим надпись, о том что пользователь запустил игру.
    print("Вы запустили игру \"Камень-Ножницы-Бумага\"")
  
    # Получаем имя игрока и создаем соот. объект
    name = input("Представтесь: ")
    self.__cur_player = Player(name)

    # Создаем объекты меню для игры
    self.__main_menu   = Menu.MainMenu()
    self.__end_menu    = Menu.EndMenu()
    self.__choice_menu = Menu.ChoiceMenu()

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
          self.__PlayGame()
          choice_menu_player = self.__ChoicePlayerInMenu(self.__end_menu)
          # Если игрок выбор выйти в главное меню, то флаг продолжения игры
          # устанавливается в False и игра выходит в главное меню
          if (choice_menu_player == GlobalConstants.END_GAME):
            f_cont_game = False

      elif (choice_menu_player == GlobalConstants.EXIT_GAME):
        f_game = False
        str_output  = "Спасибо за игру. Ваш процент выйгрышей составил: "
        str_output += str(self.__cur_player.GetWinningPercentage())
        str_output += "%. Всего доброго!"
        print(str_output)


    