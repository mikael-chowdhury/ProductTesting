from lib.ui.Button import Button
from lib.ui.Label import Label
from lib.ui.UIElement import UIElement

class UIElementHandler:
    ELEMENTS:list = [UIElement, Button, Label]

    @staticmethod
    def get_element_by_id(id:str):
        for element in UIElementHandler.ELEMENTS:
            name = element.__name__
            
            if id == name:
                return element

        return None