from flet import Column, ListView, Text

loaded_accounts = ListView(expand=True, spacing=10)


class AccountsView:
    def __init__(self):
        self.accounts = ListView(expand=True, spacing=10)

    def load_accounts_from_folder(self):
        """load session file [telethon]"""
        NotImplemented

    def remove_accounts_from_view(self):
        NotImplemented

    def sort_accounts_in_view(self):
        NotImplemented

    def render_accounts_list(self):
        for i in range(15):
            self.accounts.controls.append(Text(f"Line {i}"))
        return Column(

            controls=[
                self.accounts
            ]
        )
