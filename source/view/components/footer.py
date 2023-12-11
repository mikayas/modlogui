import flet as ft
from utils import Colors, Tags


class Footer(ft.UserControl):
    '''page footer component'''

    def __init__(self, page):
        super().__init__()
        self.page = page

    def build(self):
        return ft.Column(
            controls=[
                ft.Text(
                    value=Tags.SUBTITLE,
                    size=12,
                    color=Colors.GRAY2,
                    weight=ft.FontWeight.W_700,
                    width=self.page.window_width,
                    text_align=ft.TextAlign.CENTER,
                ),
            ],
            spacing=0,
        )

