from lib.screen.Screen import Screen
from lib.ui.UIElement import UIElement

import pygame

class MainScreen(Screen):
    def __init__(self) -> None:
        super().__init__()

        self.titletext = UIElement.from_json("MainScreen/TitleText.json")

        self.UIElements.append(self.titletext)

    def update(self, screen:pygame.Surface, events):
        screen.fill((0, 0, 0))
        super().update(screen, events)