# https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer
import pygame
# player.py
class Player:
    def __init__(self, position):
        self.can_move = True
        self.position = list(position)
        self.width = 50  # width of the player
        self.height = 50  # height of the player

    def move(self, movement):
        if self.can_move:
            self.position[0] += movement[0] * 50
            self.position[1] += movement[1] * 50

    def render(self, surface):
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], self.width, self.height))

    def collision(self, power_up):
        # Check if player rectangle intersects with the power-up rectangle
        return (
            self.position[0] < power_up.x + power_up.width and
            self.position[0] + self.width > power_up.x and
            self.position[1] < power_up.y + power_up.height and
            self.position[1] + self.height > power_up.y
        )
