from lib.screen.Screen import Screen
from lib.screen.ScreenHandler import ScreenHandler

from lib.ui.UIElement import UIElement

class SecondaryScreen(Screen):
    def __init__(self) -> None:
        super().__init__()

        self.backButton = UIElement.from_json("SecondaryScreen/BackButton.json")
        self.backButton.onclick = lambda *args: self.prev_screen()

        self.UIElements.append(self.backButton)

    def prev_screen(self):
        from screens.MainScreen import MainScreen
        ScreenHandler.switchscreen(MainScreen())

    def update(self, screen, events):
        super().update(screen, events)