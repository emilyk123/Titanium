# https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer
import pygame
class Player:
    def __init__(self, position):
        self.can_move = True
        self.position = list(position)
    
    def move(self, movement):
        if self.can_move:
            # position = [xPosition, yPosition]
            self.position[0] += movement[0] * 50
            self.position[1] += movement[1] * 50
    
    def render(self, surface):
        # Draw rectangle to the surface
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], 50, 50))