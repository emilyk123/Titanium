# Used this to set up tilemap
# https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
# https://dafluffypotato.com/assets/pg_tutorial (03_player_tiles_physics)

import os
import json
import pygame

NEIGHBOR_OFFSETS = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (0, 0), (-1, 1), (0, 1), (1, 1)]
PHYSICS_TILES = {'water'}

class Tilemap:
    def __init__(self, game, tile_size=16):
        # This will have all tiles with their type and location in a dictionary
        self.tiles = {}

        self.game = game

        self.tilemap = {}

        # This is the width and height of the tile in pixels
        self.tile_size = tile_size

    def tiles_around(self, pos):
        # List of tiles adjacent and diagonal to the position given
        tiles = []
        # Get argument pos in terms of tiles instead of pixels
        tile_loc = (int(pos[0] // self.tile_size), int(pos[1] // self.tile_size))
        # Go through list of neighbor offsets
        for offset in NEIGHBOR_OFFSETS:
            # Add offset to tile location to the current tile location as a string, tilemap location information is stored in this format
            check_loc = str(tile_loc[0] + offset[0]) + ';' + str(tile_loc[1] + offset[1])
            # If the location checked exists in tilemap, add it to the list of tiles around
            if check_loc in self.tilemap:
                tiles.append(self.tilemap[check_loc])
        return tiles
    
    def physics_rects_around(self, pos):
        rects = []
        for tile in self.tiles_around(pos):
            # Checks if the tile type is in the PHYSICS_TILES list
            if tile['type'] in PHYSICS_TILES:
                # Add the rect of the tile that is around the player to the rects list
                rects.append(pygame.Rect(tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size, self.tile_size, self.tile_size))
        # Returns list of rects that the player will interact with
        return rects

    def save(self, path):
        f = open(path, 'w')
        json.dump({'tilemap': self.tilemap, 'tile_size': self.tile_size}, f)
        f.close()
    
    def load(self, path):
        f = open(path, 'r')
        map_data = json.load(f)
        f.close()

        self.tilemap = map_data['tilemap']
        self.tile_size = map_data['tile_size']

    def render(self, surface):
        for loc in self.tilemap:
            tile = self.tilemap[loc]
            surface.blit(self.game.assets[tile['type']][tile['variant']], (tile['pos'][0] * self.tile_size, tile['pos'][1] * self.tile_size))