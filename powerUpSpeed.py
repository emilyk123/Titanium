# create a speed power up class 


import pygame 

class SpeedPowerUP(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y 
        self.effect = "speed"