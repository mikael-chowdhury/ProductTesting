from pprint import isreadable
from turtle import update
import pygame

from lib.core.IUpdateable import IUpdateable
from lib.screen.Screen import Screen

class Project(IUpdateable):
    def __init__(self, width, height) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((width, height))
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

    def update(self, screen, events):
        super().update(screen, events)