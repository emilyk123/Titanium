
import pygame
import random


class SpeedPowerUP(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.effect = "speed"
        
        # Create a basic visual representation for the power-up
        self.image = pygame.Surface((20, 20))  # Size of the power-up
        self.image.fill((255, 0, 0))  # Red color as a placeholder
        
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