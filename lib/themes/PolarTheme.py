from lib.themes.Theme import Theme

class PolarTheme(Theme):
    def __init__(self):
        super().__init__()

        self.primary = (0, 148, 202)
        self.secondary = (174, 226, 244)
        self.tertiary = (239, 250, 255)
        self.quaternery = (172, 207, 222)