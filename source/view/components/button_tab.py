import flet as ft
from utils import Colors


class Buttontab(ft.UserControl):
    '''button component for section tabs'''

    def __init__(self, text, route, page):
        super().__init__()
        self.text = text
        self.route = route
        self.page = page
        self.text_color = Colors.GRAY3
        self.border_color = Colors.GRAY1
        if self.page.route == self.route:
            self.text_color = Colors.WHITE
            self.border_color = Colors.WHITE

    def build(self):
        return [ft.Container(
            ft.TextButton(
                content=ft.Text(self.text, size=12, width=60, text_align='center'),
                on_click=lambda _: self.page.go(self.route),
                style=ft.ButtonStyle(
                    bgcolor={ft.MaterialState.DEFAULT: None},
                    color={ft.MaterialState.DEFAULT: self.text_color},
                    shape={
                        ft.MaterialState.DEFAULT: ft.RoundedRectangleBorder(radius=0),
                    },
                ),
            ),
            border=ft.border.only(
                bottom=ft.border.BorderSide(2, self.border_color),
            ),
        )]

