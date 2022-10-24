from lib.ui.UIElement import UIElement

from lib.config.UIConfig import THEME
import lib.config.WindowConfig as WindowConfig

import pygame

class Button(UIElement):
    def __init__(self, x=0, y=0, w=0, h=0, text="", font="Arial", fontSize=24, fontColour=THEME.primary, backgroundcolour=THEME.tertiary, borderColour=THEME.quaternery, backgroundimage=None, onclick=lambda *args: None, isIcon=False, draggable=True, external=False) -> None:
        super().__init__(x, y, w, h, text, font, fontSize, fontColour, backgroundcolour, borderColour, backgroundimage, draggable)

        self.onclick = onclick

        self.borderradius = 50
        self.borderwidth = 5

        self.external = external

        self.isIcon = isIcon

    def is_hovering(self, mx, my):
        return mx >= self.x and mx <= self.x + self.w and my >= self.y and my <= self.y + self.h

    def update(self, screen, events):
        super().update(screen, events, False)

        if not WindowConfig.DEBUG or self.external:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.is_hovering(event.pos[0], event.pos[1]):
                            if self.isIcon and self.mask is not None and self.loadedbackgroundimage is not None:
                                rect = self.loadedbackgroundimage.get_rect(center=self.rect.center)
                                if self.mask.has_collided(rect.x, rect.y, *event.pos):
                                    self.onclick(screen, events, event.pos)
                            else: 
                                self.onclick(screen, events, event.pos)

        self.first_load = False