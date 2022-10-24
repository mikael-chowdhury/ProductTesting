from lib.config.UIConfig import THEME
import lib.config.WindowConfig as WindowConfig

from lib.screen.Screen import Screen

import pygame

class DebuggingWindow():
    instance = None

    def __init__(self) -> None:
        pygame.init()

        self.window = pygame.display.set_mode((WindowConfig.WIDTH, WindowConfig.HEIGHT))
        self.screen = self.window

        self.isRunning = True

        self.screens: list[Screen] = []
        self.currentScreen = None

        self.tick = 0

        DebuggingWindow.instance = self

    def loop(self):
        while self.isRunning:
            events = pygame.event.get()

            self.window.fill((255, 255, 255))

            if self.currentScreen is not None:
                self.screen.fill(THEME.secondary)
                self.currentScreen.update(self.screen, events)
                
            pygame.display.update()