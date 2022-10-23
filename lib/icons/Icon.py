import pygame

import lib.icons as im

def Icon(name) -> pygame.Surface:
    im.icon_to_image(name)
    path = f"icons/{name}.svg"

    return path