import flet as ft
from ..components import Header, MenuProfiles, Buttondef, Footer
from ...controller.home import start_game, actual_profile, show_profiles
from head import Head_pages


def home(page):
    '''component for generating the home section'''
    return ft.Column(
        controls=[
            Header(page=page),
            ft.Container(
                ft.Column(
                    controls=[
                        MenuProfiles(default=actual_profile(), profiles=show_profiles(e=None)),
                        Buttondef(text='Start Game', callback=start_game),
                    ],
                ),
                alignment=ft.alignment.center,
            ),
            Footer(page=page),
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        height=Head_pages.HEIGHT,
    )

