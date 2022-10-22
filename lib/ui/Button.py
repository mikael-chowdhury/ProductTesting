from lib.ui.UIElement import UIElement

from lib.config.UIConfig import THEME
import lib.config.WindowConfig as WindowConfig

import pygame

class Button(UIElement):
    def __init__(self, x=0, y=0, w=0, h=0, text="", font="Arial", fontSize=24, fontColour=THEME.primary, backgroundcolour=THEME.tertiary, borderColour=THEME.quaternery, backgroundimage=None, onclick=lambda *args: None) -> None:
        super().__init__(x, y, w, h, text, font, fontSize, fontColour, backgroundcolour, borderColour, backgroundimage)

        self.onclick = onclick

        self.borderradius = 50
        self.borderwidth = 5

    def is_hovering(self, mx, my):
        return mx >= self.x and mx <= self.x + self.w and my >= self.y and my <= self.y + self.h

    def update(self, screen, events):
        super().update(screen, events, False)

        if not WindowConfig.DEBUG:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.is_hovering(event.pos[0], event.pos[1]):
                            self.onclick(screen, events, event.pos)

        self.first_load = False