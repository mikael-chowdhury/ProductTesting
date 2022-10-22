from lib.ui.UIElement import UIElement

from lib.config.UIConfig import THEME

class Label(UIElement):
    def __init__(self, x=0, y=0, w=0, h=0, text="", font="Arial", fontSize=24, fontColour=THEME.tertiary, backgroundcolour=THEME.primary, backgroundimage=None) -> None:
        super().__init__(x, y, w, h, text, font, fontSize, fontColour, backgroundcolour, backgroundimage)

    def update(self, screen, events):
        super().update(screen, events)