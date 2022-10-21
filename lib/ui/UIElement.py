import json
import os
import pygame

from lib.core.IUpdateable import IUpdateable
from lib.ui.anchors.RectLocation import RectLocation

from lib.util.ResourceLocation import ResourceLocation

import lib.config.RenderConfig as RenderConfig

class UIElement(IUpdateable):
    def __init__(self, x=0, y=0, w=0, h=0, text="", font="Arial", fontSize=24, fontColour=(255, 255, 255), backgroundcolour=None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.text = text
        self.lasttext = self.text

        self.font = font
        self.lastfont = self.font

        self.fontSize = fontSize
        self.lastfontsize = self.fontSize

        self.fontColour = fontColour
        self.lastfontcolour = self.fontColour

        self.load_text()

        self.anchor = None

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.backgroundcolour = backgroundcolour

        self.first_load = True

    def load_text(self):
        if self.text.strip() != "":
            self.loaded_font = pygame.font.Font(self.font, self.fontSize) if not self.font.lower() in pygame.font.get_fonts() else pygame.font.SysFont(self.font, self.fontSize)
            self.loaded_text = self.loaded_font.render(self.text, RenderConfig.ANTIALIASING, self.fontColour)

            self.lasttext = self.text
            self.lastfont = self.font
            self.lastfontsize = self.fontSize
            self.lastfontcolour = self.fontColour
        else:
            self.loaded_font = None
            self.loaded_text = None

    def anchor_element(self, loc: RectLocation):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        
        setattr(self.rect, loc.value[0], loc.value[1])

        self.x = self.rect.x
        self.y = self.rect.y
        self.w = self.rect.w
        self.h = self.rect.h
    
    def update(self, screen, events, cancel_first_load=True):
        if self.lasttext != self.text or self.lastfont != self.font or self.lastfontsize != self.fontSize or self.lastfontcolour != self.fontColour:
            self.load_text()

        if self.anchor is not None:
            self.anchor_element(RectLocation.__getitem__(self.anchor.upper()))

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        if self.backgroundcolour is not None:
            pygame.draw.rect(screen, self.backgroundcolour, self.rect)

        if self.loaded_text is not None:
            rect = self.loaded_text.get_rect(center=self.rect.center)
            screen.blit(self.loaded_text, rect)

        if cancel_first_load:
            self.first_load = False

    @staticmethod
    def from_json(path:str):
        _json = json.load(open(os.path.join(ResourceLocation("elements").__str__(), path)))

        from lib.util.handlers.UIElementHandler import UIElementHandler
        element = UIElementHandler.get_element_by_id(_json["type"])

        if element is not None:
            instance = element()

            propertyKeys = _json["properties"].keys()

            for key in propertyKeys:
                value = _json["properties"][key]

                if type(value) == str and value.startswith("eval("):
                    value = eval(value[5:-1])
                    setattr(instance, key, value)
                else:
                    setattr(instance, key, value)

            return instance

        return None