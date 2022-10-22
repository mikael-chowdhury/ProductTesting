from lib.screen.Screen import Screen
from lib.ui.UIElement import UIElement
from lib.screen.ScreenHandler import ScreenHandler

import pygame

class MainScreen(Screen):
    def __init__(self) -> None:
        super().__init__()

        self.textLabel = UIElement.from_json("MainScreen/TitleText.json")
        self.testButton = UIElement.from_json("MainScreen/TestButton.json")

        self.testButton.onclick = lambda *args: self.next_screen()

        self.UIElements.append(self.textLabel)
        self.UIElements.append(self.testButton)

    def next_screen(self):
        from screens.SecondaryScreen import SecondaryScreen
        ScreenHandler.switchscreen(SecondaryScreen())

    def update(self, screen:pygame.Surface, events):
        super().update(screen, events)