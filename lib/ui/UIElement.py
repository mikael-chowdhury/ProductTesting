import json
import os
import pygame

from lib.core.IUpdateable import IUpdateable
from lib.ui.anchors.RectLocation import RectLocation

from lib.util.ResourceLocation import ResourceLocation

class UIElement(IUpdateable):
    def __init__(self, x=0, y=0, w=0, h=0, backgroundcolour=None) -> None:
        self.x = x
        self.y = y
        self.w = w
        self.h = h

        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)
        self.backgroundcolour = backgroundcolour

    def anchor_element(self, loc: RectLocation, pos):
        rect = pygame.Rect(self.x, self.y, self.w, self.h)
        setattr(rect, loc.value, pos)
    
    def update(self, screen, events):
        self.rect = pygame.Rect(self.x, self.y, self.w, self.h)

        if self.backgroundcolour is not None:
            pygame.draw.rect(screen, (self.backgroundcolour), self.rect)

    @staticmethod
    def from_json(path:str):
        _json = json.load(open(os.path.join(ResourceLocation(f"elements"), path)))

        from lib.util.handlers.UIElementHandler import UIElementHandler
        element = UIElementHandler.get_element_by_id(_json["type"])

        if element is not None:
            instance = element()

            propertyKeys = _json["properties"].keys()

            for key in propertyKeys:
                value = _json["properties"][key]
                setattr(instance, key, value)

            return instance

        return None