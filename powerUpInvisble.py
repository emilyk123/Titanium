# create an invisble power up class 

import pygame 
import random

class InvisblePowerUp(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.effect = "invisibility"
        
        # Create a basic visual representation for the power-up
        self.image = pygame.Surface((20, 20))  # Size of the power-up
        self.image.fill((100, 100, 100))  # Grey color as a placeholder
        
        # Set position and rect for collision detection
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        # Draws the power-up on the given surface
        surface.blit(self.image, self.rect)

    def randomize_position(self, width, height):
        # Move the power-up to a new random position within screen bounds
        self.rect.x = random.randint(0, width - self.rect.width)
        self.rect.y = random.randint(0, height - self.rect.height)