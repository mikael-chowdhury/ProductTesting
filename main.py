from lib.core.Project import Project
from screens.MainScreen import MainScreen

project = Project(320, 450)

project.screens.append(MainScreen())
project.currentScreen = project.screens[0]

project.loop()