from sys import path

path.insert(0, "./")
from Rock_Papper_Scissor import Weapon

START_GAME = 0 # Константа, отвечающая за начало игры
EXIT_GAME  = 1 # Константа, отвечающая за выход с игры

CONTINUE_GAME = 10 # Константа, отвечающая за продолжение игры
RESULT_PLAYER = 11 # Константа, отвечающая за вывод меню с выбором просмотра результатов
END_GAME      = 12 # Константа, отвечающая за выход из игры в глав. меню

CHECK_COUNT_WINS      = 20 # Константа, отвечающая за просмотр кол-ва выйгр. 
CHECK_COUNT_PROC_WINS = 21 # Константа, отвечающая за просмотр проц. выйгр
CHECK_COUNT_LOSES     = 22 # Константа, отвечающая за просмотр кол-ва пройгр.
CHECK_COUNT_DRAW      = 23 # Константа, отвечающая за просмотр кол-ва ничьих

NUM_ROCK    = 100 # Константа, отвечающая за выбор камня
NUM_SCISSOR = 101 # Константа, отвечающая за выбор ножниц
NUM_PAPER   = 102 # Константа, отвечающая за выбор бумаги

ROCK_WEAP    = Weapon.Weapon(NUM_ROCK)    # Константа, оружия камня
SCISSOR_WEAP = Weapon.Weapon(NUM_SCISSOR) # Константа, оружия ножниц
PAPER_WEAP   = Weapon.Weapon(NUM_PAPER)   # Константа, оружия бумаги

DRAW         = 0 # Константа, которая описывает значение ничьи
WIN_PLAYER   = 1 # Константа, которая описывает значение победы игрока
WIN_OPPONENT = 2 # Константа, которая описывает значение победы оппонента

# Константа, отвечающая за количество знаков после запятой, у вывода результата
# процентного соот. выигрыша 
PREC_DISP_RES_WINS = 3  

# Путь до файла с результатами игроков
PATH_RESULT_PLAYER_FILE = "./"
# Имя файла с результатами игкроков в формате "*.json"
NAME_RESULT_PLAYER_FILE = "result_player.json"

# Строки, которые будут записаны в файл с количеством побед/поражений/ничьих
STR_COUNT_WINS_GAME  = "count_wins"
STR_COUNT_LOSES_GAME = "count_loses"
STR_COUNT_DRAWS_GAME = "count_draws"

# Кодировка для файла
ENCODING_FOR_FILE = "utf-8"