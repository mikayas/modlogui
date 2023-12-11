import flet as ft
from ..model.game import Game
from ..model.profile import Files, Ini
from utils import Paths


def start_game(e):
    '''starts the executable (the game)'''
    gta = Game(Paths.GAME_EXE)
    gta.run()


def actual_profile():
    '''returns the current profile'''
    profile = Ini(Paths.MODLOADER_INI)
    return profile.set_value('Folder.Config', 'Profile')


def show_profiles(e):
    '''returns a list of all profiles'''
    profiles = Files(Paths.PROFILE_DIR)
    profiles.add(0, 'Default')
    list_profiles = []

    for file in profiles.all():
        list_profiles.append(
            ft.dropdown.Option(file.replace('.ini', ''))
        )

    return list_profiles


def change_profile(value):
    '''change current profile'''
    profile = Ini(Paths.MODLOADER_INI)
    profile.change_value('Folder.Config', 'Profile', value)

