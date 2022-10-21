from lib.screen.Screen import Screen
from lib.ui.UIElement import UIElement

import pygame

class MainScreen(Screen):
    def __init__(self) -> None:
        super().__init__()

        self.UIElements.append(UIElement.from_json("MainScreen/Clicker.json"))
        print(self.UIElements)

    def update(self, screen:pygame.Surface, events):
        screen.fill((0, 0, 0))
        super().update(screen, events)