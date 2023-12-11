import flet as ft
from utils import Colors


class Buttondef(ft.UserControl):
    '''button component for executing functions'''

    def __init__(self, text, callback):
        super().__init__()
        self.text = text
        self.callback = callback

    def build(self):
        return ft.TextButton(
            content=ft.Text(self.text, weight=ft.FontWeight.W_600),
            width=200,
            height=32,
            on_click=self.callback,
            style=ft.ButtonStyle(
                bgcolor=Colors.PRIMARY1,
                color=Colors.BLACK,
                shape=ft.RoundedRectangleBorder(radius=4),
            ),
        )

