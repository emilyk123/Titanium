# Used this to set up tilemap
# https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
# https://dafluffypotato.com/assets/pg_tutorial (03_player_tiles_physics)

import os

import pygame

class Tilemap:
    def __init__(self, tile_size=16):
        # This will have all tiles with their type and location in a dictionary
        self.tiles = {}

        # This is the width and height of the tile in pixels
        self.tile_size = tile_size

        # This is a loop that creates 20 tiles in a horizontal line
        for i in range(20):
            # (x, y) the tuple holds the location
            # since the y part of the location stays the same and the x changes, they are placed horizontally
            self.tiles[str(i) + ';5'] = {'pos': (i, 5)}

    def render(self, surface):
        for loc in self.tiles:
            # Gets the value of the tilemap dictionary
            tile = self.tiles[loc]

            # Finds the sprite for the water image
            image = pygame.image.load('sprites/water.png').convert()

            # Blit the image onto the surface
            # Multiply the position by the tile_size to have the tiles placed next to each other and not overlapping
            surface.blit(image, (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))