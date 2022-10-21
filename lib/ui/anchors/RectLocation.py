from enum import Enum

import lib.config.WindowConfig as WindowConfig

class RectLocation(Enum):
    TOPLEFT = ["topleft", [0, 0]]
    TOPRIGHT = ["topright", [WindowConfig.WIDTH, 0]]
    BOTTOMLEFT = ["bottomleft", [0, WindowConfig.HEIGHT]]
    BOTTOMRIGHT = ["bottomright", [WindowConfig.WIDTH, WindowConfig.HEIGHT]]
    MIDDLE = ["center", [int(WindowConfig.WIDTH / 2), int(WindowConfig.HEIGHT / 2)]]