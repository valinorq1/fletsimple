from components.accounts import AccountsView, loaded_accounts
from components.sidebar import Sidebar

import flet as ft


class HomeScreen(ft.UserControl, AccountsView, Sidebar):

    def build(self):
        self.loaded_accounts = ft.Column()
        self.loaded_proxy = ft.Column()

        return ft.Column(
            width=1100,
            height=600,
            controls=[
                ft.Row(
                    controls=[
                        Sidebar().render(),
                        ft.VerticalDivider(width=1),
                        loaded_accounts,
                        self.render_accounts_list()
                    ],
                    expand=True
                )
            ]
        )


def main(page: ft.Page):
    page.title = "TService - Работа с аккаунтами"
    page.horizontal_alignment = "start"
    page.update()

    # create application instance
    tapp = HomeScreen()

    # add application's root control to the page
    page.add(tapp)


if __name__ == '__main__':
    ft.flet.app(target=main)
