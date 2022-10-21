from lib.ui.UIElement import UIElement

import pygame

from lib.ui.text.TextObject import TextObject

class Button(UIElement):
    def __init__(self, x=0, y=0, w=0, h=0, textObj:TextObject=None, backgroundcolour=None, onclick=lambda *args: None) -> None:
        super().__init__(x, y, w, h, backgroundcolour)

        self.textObj = textObj
        self.onclick = onclick

    def is_hovering(self, mx, my):
        return mx >= self.x and mx <= self.x + self.w and my >= self.y and my <= self.y + self.h

    def update(self, screen, events):
        super().update(screen, events)

        if self.textObj is not None:
            rect = self.textObj.loaded_text.get_rect(center=self.rect)
            screen.blit(self.textObj.loaded_text, rect)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.is_hovering(event.pos[0], event.pos[1]):
                        self.onclick(screen, events, event.pos)