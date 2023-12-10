import flet as ft
from routes import routes
from head import head


def main(page: ft.Page):
    head(page=page)
    page.on_route_change = routes(page=page, route=any)
    page.go(page.route)


ft.app(target=main)

