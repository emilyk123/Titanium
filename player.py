# Used to help set up Player class
# https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
# https://dafluffypotato.com/assets/pg_tutorial

import pygame
class Player:
    def __init__(self, position):
        # After the player moves, this is set to false until the timer sets it back to true
        self.can_move = True
        self.position = list(position)
        self.size = (16, 16)
        self.health = 3

    def rect(self):
        # Returns player rect
        return pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    
    def move(self, tilemap, movement, game):
        if self.can_move:
            # position = [xPosition, yPosition]
            self.position[0] += movement[0] * 16

            self.position[1] += movement[1] * 16
            
            player_rect = self.rect()
            for rect in tilemap.physics_rects_around(self.position):
                # Checks if the player rect collided with one of rects in physics_rects_around
                if player_rect.colliderect(rect):
                    self.position = list(game.spawn_position)
                    # If health isn't at zero, decrease the player health by 1 when player goes in water
                    if self.health != 0:
                        self.health -= 1
    
    def render(self, surface):
        # Draw rectangle to the surface
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], 16, 16))