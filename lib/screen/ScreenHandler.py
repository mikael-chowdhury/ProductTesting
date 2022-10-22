from lib.core.Project import Project
from lib.screen.Screen import Screen

class ScreenHandler:
    @staticmethod
    def switchscreen(newscreen:Screen):
        Project.instance.currentScreen = newscreen

    @staticmethod
    def defswitchscreen(newscreen:Screen):
        return (lambda *args: ScreenHandler.switchscreen(newscreen))