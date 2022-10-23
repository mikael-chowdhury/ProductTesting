import lib.config.RenderConfig as RenderConfig

class VaryingText():
    def __init__(self, text, colour, font) -> None:
        self.text = text
        self.lasttext = self.text
        self.loaded_text = None

        self.colour = colour
        self.font = font

        self.load_text()

    def load_text(self):
        self.loaded_text = self.font.render(self.text, RenderConfig.ANTIALIASING, self.colour)

    def update(self):
        if self.text != self.lasttext:
            self.lasttext = self.text
            self.load_text()