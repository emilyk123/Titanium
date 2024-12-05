import pygame
import random
# Import random module for random operations
from tilemap import Tilemap

class PowerUp:
    def __init__(self, screen_width, screen_height, tilemap):
        self.screen_width = screen_width
        self.screen_height = screen_height
        #
        self.tilemap = tilemap


        self.color = (255, 0, 0)
        self.width = 16
        self.height = 16

        # Set initial random position
        #*self.x = random.randint(0, self.screen_width - self.width) #***********
        #*self.y = random.randint(0, self.screen_height - self.height)
        self.randomize_position()

    def draw(self, surface):
        # Draw the power-up at its current position
        pygame.draw.rect(surface, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    #----------------------------------------
    #def randomize_position(self):
    #    tile_x = random.randint(0, self.screen_width // self.tilemap.tile_size - 1)
    #    tile_y = random.randint(0, self.screen_height // self.tilemap.tile_size - 1)
    #    self.x = tile_x * self.tilemap.tile_size
    #    self.y = tile_y * self.tilemap.tile_size

    def randomize_position(self):
    # Loop until a non-water tile position is found
        max_attempts = 100

        for attempt in range(max_attempts):
            tile_x = random.randint(0, self.screen_width // self.tilemap.tile_size - 1)
            tile_y = random.randint(0, self.screen_height // self.tilemap.tile_size - 1)
            position = (tile_x * self.tilemap.tile_size, tile_y * self.tilemap.tile_size)
            tile_type = self.tilemap.get_tile_type(position)

            if tile_type != 'water':
                self.x, self.y = position
                return  # Exits once a valid position is found

    # If no valid tile is found after max_attempts, print a warning
        print("Warning: Could not find a non-water tile for the power-up.")


    def collision(self, other):
        return (
            self.x < other.x + other.width and
            self.x + self.width > other.x and
            self.y < other.y + other.height and
            self.y + self.height > other.y
        )
        