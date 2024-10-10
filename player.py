# # https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer
# import pygame
# class Player:
#     def __init__(self, position):
#         self.can_move = True
#         self.position = list(position)
    
#     def move(self, movement):
#         if self.can_move:
#             # position = [xPosition, yPosition]
#             self.position[0] += movement[0] * 50
#             self.position[1] += movement[1] * 50
    
#     def render(self, surface):
#         # Draw rectangle to the surface
#         pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], 50, 50))


import pygame

class Player:
    def __init__(self, position):
        self.can_move = True
        self.position = list(position)
        # Create a rect for the player object
        self.rect = pygame.Rect(self.position[0], self.position[1], 50, 50)  # 50x50 is the size of the player

    def move(self, movement):
        if self.can_move:
            # Update position
            self.position[0] += movement[0] * 50
            self.position[1] += movement[1] * 50
            # Update the rect's position
            self.rect.topleft = self.position

    def render(self, surface):
        # Update rect's position before drawing (in case it changed)
        self.rect.topleft = self.position
        # Draw the player using the rect
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), self.rect)
