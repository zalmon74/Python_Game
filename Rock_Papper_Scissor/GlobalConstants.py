from Weapon import Weapon

START_GAME = 0 # Константа, отвечающая за начало игры
EXIT_GAME  = 1 # Константа, отвечающая за выход с игры

CONTINUE_GAME = 10 # Константа, отвечающая за продолжение игры
END_GAME      = 11 # Константа, отвечающая за выход из игры в глав. меню

NUM_ROCK    = 100 # Константа, отвечающая за выбор камня
NUM_SCISSOR = 101 # Константа, отвечающая за выбор ножниц
NUM_PAPER   = 102 # Константа, отвечающая за выбор бумаги

ROCK_WEAP    = Weapon(NUM_ROCK)    # Константа, оружия камня
SCISSOR_WEAP = Weapon(NUM_SCISSOR) # Константа, оружия ножниц
PAPER_WEAP   = Weapon(NUM_PAPER)   # Константа, оружия бумаги

DRAW         = 0 # Константа, которая описывает значение ничьи
WIN_PLAYER   = 1 # Константа, которая описывает значение победы игрока
WIN_OPPONENT = 2 # Константа, которая описывает значение победы оппонента

# Константа, отвечающая за количество знаков после запятой, у вывода результата
# процентного соот. выигрыша 
PREC_DISP_RES_WINS = 3  