# Used to help set up Player class
# https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
# https://dafluffypotato.com/assets/pg_tutorial

import pygame
# player.py
class Player:
    def __init__(self, position):
        # After the player moves, this is set to false until the timer sets it back to true
        self.can_move = True
        self.position = list(position)
        self.size = (16, 16)
        self.health = 3
        self.width = 16  # width of the player
        self.height = 16  # height of the player
        self.is_alive = True

    def rect(self):
        # Returns player rect
        return pygame.Rect(self.position[0], self.position[1], self.size[0], self.size[1])
    
    def move(self, tilemap, movement, game, mover_rect):
        if self.can_move:
            # position = [xPosition, yPosition]
            self.position[0] += movement[0] * 16

            self.position[1] += movement[1] * 16
            
            player_rect = self.rect()
            for rect in tilemap.physics_rects_around(self.position):
                # Checks if the player rect collided with one of rects in physics_rects_around
                if player_rect.colliderect(rect) and not player_rect.colliderect(mover_rect):
                    self.position = list(game.spawn_position)
                    # If health isn't at zero, decrease the player health by 1 when player goes in water
                    if self.health != 0:
                        self.health -= 1
                        if self.health == 0:
                            self.is_alive = False
    
    def render(self, surface):
        # Draw rectangle to the surface
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], 16, 16))
    
    def collision(self, power_up):
        # Check if player rectangle intersects with the power-up rectangle
        return (
            self.position[0] < power_up.x + power_up.width and
            self.position[0] + self.width > power_up.x and
            self.position[1] < power_up.y + power_up.height and
            self.position[1] + self.height > power_up.y
        )
