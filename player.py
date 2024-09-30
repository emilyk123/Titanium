# Used to help set up Player class
# https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
# https://dafluffypotato.com/assets/pg_tutorial

import pygame
class Player:
    def __init__(self, position):
        # After the player moves, this is set to false until the timer sets it back to true
        self.can_move = True
        self.position = list(position)
    
    def move(self, movement):
        if self.can_move:
            # position = [xPosition, yPosition]
            self.position[0] += movement[0] * 16
            self.position[1] += movement[1] * 16
    
    def render(self, surface):
        # Draw rectangle to the surface
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], 16, 16))