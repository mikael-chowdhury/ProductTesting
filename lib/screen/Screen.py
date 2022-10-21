from lib.core.IUpdateable import IUpdateable
from lib.ui.UIElement import UIElement

class Screen(IUpdateable):
    def __init__(self) -> None:
        super().__init__()

        self.UIElements:list[UIElement] = []

    def update(self, screen, events):
        for element in self.UIElements:
            element.update(screen, events)