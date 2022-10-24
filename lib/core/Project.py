import pygame
from lib.core.DebuggingWindow import DebuggingWindow

from lib.screen.Screen import Screen

import lib.config.WindowConfig as WindowConfig
import lib.config.RenderConfig as RenderConfig
from lib.config.UIConfig import THEME
from lib.ui.anchors.RectLocation import RectLocation
from lib.ui.text.VaryingText import VaryingText

from lib.ui.Button import Button

class Project:
    instance = None

    def __init__(self, debug=WindowConfig.DEBUG) -> None:
        pygame.init()

        WindowConfig.DEBUG = debug

        if WindowConfig.DEBUG:
            self.window = pygame.display.set_mode((WindowConfig.WIDTH+WindowConfig.DEBUG_PANEL_SIZE_RIGHT, WindowConfig.HEIGHT+WindowConfig.DEBUG_PANEL_SIZE_BOTTOM))
            self.screen = self.window.subsurface(pygame.Rect(0, 0, WindowConfig.WIDTH, WindowConfig.HEIGHT))
        else:
            self.window = pygame.display.set_mode((WindowConfig.WIDTH, WindowConfig.HEIGHT))
            self.screen = self.window

        self.isRunning = True

        self.screens: list[Screen] = []
        self.currentScreen = None

        self.infofont = pygame.font.SysFont("Arial", 16)

        self.mousepos = VaryingText(f"x0 y0", (0, 0, 0), self.infofont)
        self.selected_element_properties = []

        self.selected_element = None
        self.selected_element_index = -1

        self.tick = 0

        self.debugging_button = Button(text="DEBUG", w=125, h=50, draggable=False, external=True, onclick=lambda *args: self.open_debugging_window())
        self.debugging_button.rect.topright = (WindowConfig.WIDTH+WindowConfig.DEBUG_PANEL_SIZE_RIGHT - 5, 5)
        self.debugging_button.x = self.debugging_button.rect.x
        self.debugging_button.y = self.debugging_button.rect.y

        Project.instance = self

    def open_debugging_window(self):
        DebuggingWindow()

    def loop(self):
        while self.isRunning:
            events = pygame.event.get()
            keys = pygame.key.get_pressed()

            for event in events:
                if event.type == pygame.QUIT:
                    self.isRunning = False

                if self.selected_element is not None:
                    if event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]:
                            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                                v = [pygame.K_LEFT, "", pygame.K_RIGHT].index(event.key) - 1
                                self.currentScreen.UIElements[self.selected_element_index].x += v
                            
                            if event.key in [pygame.K_UP, pygame.K_DOWN]:
                                v = [pygame.K_UP, "", pygame.K_DOWN].index(event.key) - 1
                                self.currentScreen.UIElements[self.selected_element_index].y += v


                if event.type == pygame.MOUSEBUTTONDOWN:
                    for i, element in enumerate(self.currentScreen.UIElements):
                        mx, my = event.pos

                        if mx >= element.x and mx <= element.x + element.w and my >= element.y and my <= element.y + element.h:
                            self.selected_element = element
                            self.selected_element_index = i
                            self.selected_element_properties.clear()

                            for field in self.selected_element.serializable_properties:
                                self.selected_element_properties.append(self.infofont.render(f"{field}  =  {getattr(self.selected_element, field)}", RenderConfig.ANTIALIASING, (0, 0, 0)))

                            break
                        else:
                            self.selected_element = None
                            self.selected_element_index = -1
                            self.selected_element_properties.clear()

            self.tick += 1

            if self.tick >= 10:
                self.tick = 0

                if self.selected_element is not None:
                    self.selected_element_properties.clear()

                    for field in self.selected_element.serializable_properties:
                        self.selected_element_properties.append(self.infofont.render(f"{field}  =  {getattr(self.selected_element, field)}", RenderConfig.ANTIALIASING, (0, 0, 0)))

            self.window.fill((255, 255, 255))

            if self.currentScreen is not None:
                self.screen.fill(THEME.secondary)
                self.currentScreen.update(self.screen, events)

            self.mousepos.text = f"x{pygame.mouse.get_pos()[0]} y{pygame.mouse.get_pos()[1]}"
            self.mousepos.update()

            if WindowConfig.DEBUG:
                self.window.blit(self.mousepos.loaded_text, (5, WindowConfig.HEIGHT + 5))

                rect = pygame.Rect(self.screen.get_rect().right + 5, 15, 0, 0)
                for property in self.selected_element_properties:
                    self.window.blit(property, rect)
                    rect.y += 35

            self.debugging_button.update(self.window, events)
            
            pygame.display.update()