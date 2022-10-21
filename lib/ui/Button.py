from lib.ui.UIElement import UIElement

import pygame

class Button(UIElement):
    def __init__(self, x=0, y=0, w=0, h=0, text="", font="Arial", fontSize=24, fontColour=(255, 255, 255), backgroundcolour=None, onclick=lambda *args: None) -> None:
        super().__init__(x, y, w, h, text, font, fontSize, fontColour, backgroundcolour)

        self.onclick = onclick

    def is_hovering(self, mx, my):
        return mx >= self.x and mx <= self.x + self.w and my >= self.y and my <= self.y + self.h

    def update(self, screen, events):
        super().update(screen, events, False)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.is_hovering(event.pos[0], event.pos[1]):
                        self.onclick(screen, events, event.pos)

        self.first_load = False