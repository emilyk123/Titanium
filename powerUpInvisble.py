# create an invisble power up class 

import pygame 


class InvisblePowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y 
        self.effect = "invisibility"