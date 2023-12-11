import flet as ft
from utils import Colors
from ...controller.home import change_profile


class MenuProfiles(ft.UserControl):
    def __init__(self, default, profiles:list):
        super().__init__()
        self.default = default
        self.profiles = profiles

    def build(self):
        def set_profile(e):
            change_profile(dropdown.value)

        dropdown = ft.Dropdown(
            label="Profile",
            value=self.default,
            on_change=set_profile,
            options=self.profiles,
            border_color=Colors.PRIMARY1,
            border_radius=4,
            border_width=2,
            bgcolor=None,
            color=Colors.PRIMARY1,
            text_size=16,
            width=200,
            height=32,
            content_padding=10
        )

        return dropdown

