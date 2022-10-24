from socket import SO_RCVBUF
import pygame


class UIMask:
    def __init__(self, surf:pygame.Surface, thresh:int):
        self.surf = surf
        self.thresh = thresh

        self.w = self.surf.get_width()
        self.h = self.surf.get_height()

    def has_collided(self, x1, y1, x2, y2):
        collided = False
        if x2 >= x1 and x2 <= x1 + self.w and y2 >= y1 and y2 <= y1 + self.h:
            offsetx = x2-x1
            offsety = y2-y1
            alpha = self.surf.get_at([offsetx, offsety])[3]
            collided = alpha >= self.thresh
        
        return collided