import os
from lib.core.IUpdateable import IUpdateable
from lib.ui.UIElement import UIElement
from lib.util.ResourceLocation import ResourceLocation

class Screen(IUpdateable):
    def __init__(self) -> None:
        super().__init__()

        self.UIElements:list[UIElement] = []

    def update(self, screen, events):
        for element in self.UIElements:
            element.update(screen, events)

    def load_ui(self, dirpath:str, include:list[str]):
        dir = os.path.join(ResourceLocation(f"elements"), dirpath)

        for file in os.listdir(dir):
            if file in include:
                element = UIElement.from_json(os.path.join(dir, file))
                if element is not None:
                    self.UIElements.append(element)