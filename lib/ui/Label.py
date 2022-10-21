from lib.ui.UIElement import UIElement

class Label(UIElement):
    def __init__(self, x=0, y=0, w=0, h=0, text="", font="Arial", fontSize=24, fontColour=(255, 255, 255), backgroundcolour=None) -> None:
        super().__init__(x, y, w, h, text, font, fontSize, fontColour, backgroundcolour)

    def update(self, screen, events):
        super().update(screen, events)