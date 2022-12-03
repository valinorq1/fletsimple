import flet as ft
from flet import (Icon, NavigationRail, NavigationRailDestination,
                  NavigationRailLabelType, Text, icons)


class Sidebar:

    def render(self):
        return NavigationRail(
            selected_index=0,
            label_type=NavigationRailLabelType.ALL,
            # extended=True,
            min_width=100,
            min_extended_width=400,

            group_alignment=-0.9,
            destinations=[
                NavigationRailDestination(
                    icon=icons.SUPERVISED_USER_CIRCLE, selected_icon=icons.SUPERVISED_USER_CIRCLE, label="Аккаунты"
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.CELL_WIFI_OUTLINED),
                    selected_icon_content=Icon(icons.CELL_WIFI_OUTLINED),
                    label="Прокси",
                ),
                NavigationRailDestination(
                    icon=icons.SETTINGS_OUTLINED,
                    selected_icon_content=Icon(icons.SETTINGS),
                    label_content=Text("Настройки"),
                ),
            ],
            on_change=lambda e: print("Selected destination:",
                                      e.control.selected_index),
        )
