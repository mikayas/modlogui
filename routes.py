import flet as ft
from source.view.pages import home


def routes(page, route):
    '''manages the routes of the application sections'''

    page.views.clear()
    page.views.append(
        ft.View(
            route="/",
            controls=[home(page=page)],
            vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
    )
    if page.route == "/setup":
        page.views.append(
            ft.View(
                route="/setup",
                controls=[ft.Text('router setup')],
                vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            ),
        )
    if page.route == '/about':
        print('init')
        page.views.append(
            ft.View(
                route="/about",
                controls=[ft.Text('router about')],
                vertical_alignment=ft.MainAxisAlignment.SPACE_BETWEEN
            )
        )
        print('final')
    page.update()

