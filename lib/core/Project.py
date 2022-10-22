import pygame

from lib.screen.Screen import Screen

import lib.config.WindowConfig as WindowConfig
import lib.config.RenderConfig as RenderConfig
from lib.config.UIConfig import THEME

class Project:
    instance = None

    def __init__(self, debug=WindowConfig.DEBUG) -> None:
        pygame.init()

        if WindowConfig.DEBUG:
            self.window = pygame.display.set_mode((WindowConfig.WIDTH+150, WindowConfig.HEIGHT+150))
            self.screen = self.window.subsurface(pygame.Rect(0, 0, WindowConfig.WIDTH, WindowConfig.HEIGHT))
            
        else:
            self.window = pygame.display.set_mode((WindowConfig.WIDTH, WindowConfig.HEIGHT))
            self.screen = self.window

        self.isRunning = True

        self.screens: list[Screen] = []
        self.currentScreen = None

        self.infofont = pygame.font.SysFont("Arial", 16)

        self.mousepos = pygame.mouse.get_pos()
        self.lastmousepos = self.mousepos
        self.mousepostext = self.infofont.render(f"x{self.mousepos[0]} y{self.mousepos[1]}", RenderConfig.ANTIALIASING, (0, 0, 0))

        self.hovering_element = ""
        self.lasthovering_element = self.hovering_element
        self.hovering_elementtext = self.infofont.render(f"hovering: {self.hovering_element}", RenderConfig.ANTIALIASING, (0, 0, 0))
        
        Project.instance = self

    def loop(self):
        while self.isRunning:
            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.window.fill((255, 255, 255))

            if self.currentScreen is not None:
                self.screen.fill(THEME.secondary)
                self.currentScreen.update(self.screen, events)

                hovered_element = False
                for element in self.currentScreen.UIElements:
                    if element.rect.collidepoint(self.mousepos):
                        self.hovering_element = element.id
                        hovered_element = True

                if not hovered_element:
                    self.hovering_element = ""

            self.mousepos = pygame.mouse.get_pos()

            if self.mousepos != self.lastmousepos:
                if WindowConfig.DEBUG:
                    self.mousepostext = self.infofont.render(f"x{self.mousepos[0]} y{self.mousepos[1]}", RenderConfig.ANTIALIASING, (0, 0, 0))

                self.lastmousepos = self.mousepos

            if self.hovering_element != self.lasthovering_element:
                if WindowConfig.DEBUG:
                    self.hovering_elementtext = self.infofont.render(f"hovering: {self.hovering_element}", RenderConfig.ANTIALIASING, (0, 0, 0))
                self.lasthovering_element = self.hovering_element
                
            if WindowConfig.DEBUG:
                self.window.blit(self.mousepostext, (5, WindowConfig.HEIGHT + 5))
                self.window.blit(self.hovering_elementtext, (5, WindowConfig.HEIGHT + 20))
            
            pygame.display.update()