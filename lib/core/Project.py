import pygame

from lib.screen.Screen import Screen

import lib.config.WindowConfig as WindowConfig

class Project:
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((WindowConfig.WIDTH, WindowConfig.HEIGHT))
        self.isRunning = True

        self.screens: list[Screen] = []
        self.currentScreen = None

    def loop(self):
        while self.isRunning:
            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    self.isRunning = False

            if self.currentScreen is not None:
                self.currentScreen.update(self.screen, events)
            
            pygame.display.update()