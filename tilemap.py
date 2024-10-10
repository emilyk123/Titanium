# Used this to set up tilemap
# https://www.youtube.com/watch?v=2gABYM5M0ww&t=2642s&ab_channel=DaFluffyPotato
# https://dafluffypotato.com/assets/pg_tutorial (03_player_tiles_physics)

import os
import json
import pygame

class Tilemap:
    def __init__(self, game, tile_size=16):
        # This will have all tiles with their type and location in a dictionary
        self.tiles = {}

        self.game = game

        self.tilemap = {}

        # This is the width and height of the tile in pixels
        self.tile_size = tile_size

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