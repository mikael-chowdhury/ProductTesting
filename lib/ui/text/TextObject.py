import pygame

import lib.config.RenderConfig as RenderConfig

class TextObject:
    def __init__(self, text="", font="Arial", fontSize=24) -> None:
        self.text = text
        self.font = font
        self.fontSize = fontSize

        self.loaded_font = pygame.font.Font(font, fontSize)
        self.loaded_text = self.loaded_font.render(self.text, RenderConfig.ANTIALIASING)