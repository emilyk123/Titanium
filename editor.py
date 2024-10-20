# https://dafluffypotato.com/assets/pg_tutorial (07_level_editor)
# https://www.youtube.com/watch?v=2gABYM5M0ww&t=424s&ab_channel=DaFluffyPotato

# This is the level editor that uses the tilemap

import sys
import os

import pygame

from utils import load_images
from tilemap import Tilemap

# Since display is half the size of screen, this is used to adjust the position from the screen size to the display size
RENDER_SCALE = 2.0

class Editor:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('editor')

        # This is the size of the window
        self.screen = pygame.display.set_mode((640, 480))

        # This is the surface drawn to and then later scaled up to the window
        # This allows the 16x16 sprites to look larger
        self.display = pygame.Surface((320, 240))

        self.clock = pygame.time.Clock()

        # Each key in the assets dictionary is the group name and the values are the variants of the group
        self.assets = {
            'ground': load_images('ground'),
            'water': load_images('water'),
        }

        # Creates the tilemap
        self.tilemap = Tilemap(self, tile_size=16)

        # Checks to see if the file exists, if not then it doesn't load the map
        try:
            self.tilemap.load('map.json')
        except FileNotFoundError:
            pass

        # tile_list puts the group names into a list so the groups names have indexs
        self.tile_list = list(self.assets)
        # tile_group is the index that tile_list uses. It keeps track of which group of sprites is currently being used
        self.tile_group = 0
        # tile_variant is the index of the value of the group. It keeps track of which variant is currently being used
        self.tile_variant = 0

        # Keeps track if the left mouse button is clicked
        self.clicking = False
        # Keeps track if the right mouse button is clicked
        self.right_clicking = False

        # Keeps track if the left shift button is pressed
        self.shift = False

        # Keeps track of when user wants to select a new tile
        self.select_new_tile = False

        # Stores rects for display rects to if a mouse clicks one of them
        self.display_rects = {0: [],
                              1: []}

        # Stores the mouse's current position
        self.mpos = pygame.mouse.get_pos()


        # Loop used to create a dictionary of the display tiles that will help allow the user click the tile they want to draw with

        # Stores local value for the current x value position for the display tiles 
        tiles_display_x_pos = 0
        # Stores local value for the current variant
        variant = 0

        # Loops through tile groups
        for tile_group in self.tile_list:
            # Loops through variants in tile groups
            for variants in self.assets[tile_group]:
                # If current tile group is ground, then append the tile to the display_rects
                if tile_group == 'ground':
                    self.display_rects[0].append({variant: pygame.Rect(tiles_display_x_pos * 2 / RENDER_SCALE, 0, 16, 16)})
                else:
                    self.display_rects[1].append({variant - len(self.assets[self.tile_list[0]]): pygame.Rect(tiles_display_x_pos * 2 / RENDER_SCALE, 0, 16, 16)})
                variant += 1
                # Update the next tile's position
                tiles_display_x_pos += 16

    def run(self):
        while True:
            # Create black background
            self.display.fill((0, 0, 0))

            # During the first loop this draws the tiles that were loaded in if the file existed
            # After the first loop, it draws the new tiles that have been drawn to the screen from the last frame
            self.tilemap.render(self.display)

            # This is the current sprite that has been selected with a decreases opacity
            current_tile_img = self.assets[self.tile_list[self.tile_group]][self.tile_variant].copy()
            current_tile_img.set_alpha(100)

            # This gets the mouse position in the window and scales it to the size of the display surface from the window size
            self.mpos = pygame.mouse.get_pos()
            self.mpos = (self.mpos[0] / RENDER_SCALE, self.mpos[1] / RENDER_SCALE)

            # This calculates where the tile should go according to the mouse position and which part of the grid it is on
            tile_pos = (int(self.mpos[0] // self.tilemap.tile_size), int(self.mpos[1]) // self.tilemap.tile_size)

            # Draws tile to screen where the mouse is if the user isn't selecting a new tile
            if not self.select_new_tile:
                self.display.blit(current_tile_img, (tile_pos[0] * self.tilemap.tile_size, tile_pos[1] * self.tilemap.tile_size))

            # This creates tiles by adding it to the tilemap. If the left mouse button is pressed, save the location of where the tile is being placed and information about it
            if self.clicking:
                self.tilemap.tilemap[str(tile_pos[0]) + ';' + str(tile_pos[1])] = {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos}

            # This deletes tiles. If the right mouse button is pressed, delete the tile where the mouse is by removing it from the tilemap
            if self.right_clicking:
                tile_loc = str(tile_pos[0]) + ';' + str(tile_pos[1])
                if tile_loc in self.tilemap.tilemap:
                    del self.tilemap.tilemap[tile_loc]

            if self.select_new_tile:
                # Draws all of the tile options at top left screen
                tiles_display_x_pos = 0
                # Loop through tile groups
                for tile_group in self.tile_list:
                    # Loop through tile variants in the group
                    for variants in self.assets[tile_group]:
                        # Draw the current tile to the screen
                        self.display.blit(variants.copy(), (tiles_display_x_pos, 0))
                        # Update the next tile's position
                        tiles_display_x_pos += 16

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # Left mouse click
                    if event.button == 1:
                        # If the player isn't selecting a new tile, allow them to draw again
                        if not self.select_new_tile:
                            self.clicking = True
                        # Else, don't let them draw
                        else:
                            # Loop through the groups of sprites
                            for group in self.display_rects:
                                display_index = 0
                                # Loop through the groups of variants in the group
                                for variant in self.display_rects[group]:
                                    # Loop through the dictonarys inside of the current group index, contains {variant_index: rect}
                                    for variant_index in variant:
                                        # If the mouse is inside of a rect, then update the tile_variant and tile_group
                                        if pygame.Rect.collidepoint(variant[variant_index], self.mpos):
                                            self.tile_variant = variant_index
                                            self.tile_group = group
                                display_index += 1
                    # Right mouse click
                    if event.button == 3:
                        self.right_clicking = True
                
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        self.clicking = False
                    if event.button == 3:
                        self.right_clicking = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LSHIFT:
                        self.select_new_tile = True
                    # When the 's' button is pressed, everything currently drawn in the editor is saved in a json file
                    if event.key == pygame.K_s:
                        self.tilemap.save('map.json')
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LSHIFT:
                        self.select_new_tile = False

            # Scale up the display to the screen size
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

Editor().run()