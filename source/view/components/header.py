import flet as ft
from .button_tab import Buttontab


class Header(ft.UserControl):
    '''header bar component with sections'''

    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return [ft.Container(
            ft.Row(
                controls=[
                    Buttontab(text='home', route='/', page=self.page),
                    Buttontab(text='setup', route='/setup', page=self.page),
                    Buttontab(text='about', route='/about', page=self.page),
                ],
                spacing=8, alignment=ft.MainAxisAlignment.CENTER,
            ),
        ),]

