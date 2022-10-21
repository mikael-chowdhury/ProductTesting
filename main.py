from lib.core.Project import Project
from screens.MainScreen import MainScreen

project = Project()

project.screens.append(MainScreen())
project.currentScreen = project.screens[0]

project.loop()