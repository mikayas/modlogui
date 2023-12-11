import configparser as cfparser

config = cfparser.ConfigParser()

config.read('paths.ini')

GAME = config['Home.Fullpaths']['game']
MODLOADER = config['Home.Fullpaths']['modloader']


class Paths:
    GAME_EXE = GAME + config['Game.Childs']['game_exe']
    PROFILE_DIR = MODLOADER + config['Modloader.Childs']['profiles_ini']
    MODLOADER_INI = MODLOADER + config['Modloader.Childs']['modloader_ini']

