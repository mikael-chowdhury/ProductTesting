from lib.core.DebuggingWindow import DebuggingWindow
from lib.core.Project import Project
from lib.screen.Screen import Screen

import lib.config.WindowConfig as WindowConfig

class ScreenHandler:
    @staticmethod
    def switchscreen(newscreen:Screen):
        p = DebuggingWindow if WindowConfig.DEBUGGING else Project
        p.instance.currentScreen = newscreen

    @staticmethod
    def defswitchscreen(newscreen:Screen):
        return (lambda *args: ScreenHandler.switchscreen(newscreen))