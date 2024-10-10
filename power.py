import pygame
import random

class PowerUp:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

        # Initialize color and size
        self.color = (255, 0, 0)
        self.width = 60
        self.height = 60

        # Set initial random position
        self.x = random.randint(0, self.screen_width - self.width) #***********
        self.y = random.randint(0, self.screen_height - self.height)

    def draw(self, surface):
        # Draw the power-up at its current position
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def randomize_position(self):
        # Set a new random position within the screen bounds
        self.x = random.randint(0, self.screen_width - self.width) #***********
        self.y = random.randint(0, self.screen_height - self.height)