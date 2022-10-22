import pygame

from lib.screen.Screen import Screen

import lib.config.WindowConfig as WindowConfig
from lib.config.UIConfig import THEME

class Project:
    instance = None

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((WindowConfig.WIDTH, WindowConfig.HEIGHT))
        self.isRunning = True

        self.screens: list[Screen] = []
        self.currentScreen = None

        Project.instance = self

    def loop(self):
        while self.isRunning:
            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    self.isRunning = False

            if self.currentScreen is not None:
                self.screen.fill(THEME.secondary)
                self.currentScreen.update(self.screen, events)
            
            pygame.display.update()