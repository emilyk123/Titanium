# Used tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&list=LL&index=5&t=2735s&ab_channel=DaFluffyPotato
# How to create custom events: https://stackoverflow.com/questions/24475718/pygame-custom-event
# How to create a timer: https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer

import sys
import pygame
from player import Player
from tilemap import Tilemap
from object import MovingRectangle

class Game:
    def __init__(self):
        pygame.init() 

        screen_width = 640
        screen_height = 480

        display_width = 320
        display_height = 240
        # Create game window
        self.display = pygame.Surface((display_width, display_height))

        self.screen = pygame.display.set_mode((screen_width, screen_height))
        # Create clock used to limit frame rate
        self.clock = pygame.time.Clock()
        # Create custom event
        self.player_move_event = pygame.USEREVENT + 1
        # [Up, Left, Down, Right]
        self.player_movement = [False, False, False, False]

        # Create player at position 32, 32
        self.player = Player((32, 32))

        # Initialize the tilemap
        self.tilemap = Tilemap(self)
    
        # instance 
        self.mover = MovingRectangle(x=display_width, y=64, width=64, height=16, speed=-2) 

    def run(self):
        # Every 3 millisecond the player can move
        pygame.time.set_timer(self.player_move_event, 200)

        while True:
            # Checks all key and mouse presses
            for event in pygame.event.get():
                # Pressing the red x at the corner or the window closes the game
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # Allow player to move
                if event.type == self.player_move_event:
                    self.player.can_move = True
                
                # Check for input with WASD or the arrow keys
                if event.type == pygame.KEYDOWN:
                    # If timer has passed time limit, allow player input
                    if self.player.can_move:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            self.player_movement[0] = True
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            self.player_movement[1] = True
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                            self.player_movement[2] = True
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            self.player_movement[3] = True
                        
                        # Subtract player_movement[3] (Right) from player_movement[1] (Left) to get horizontal direction
                        # Subtract player_movement[2] (Down) from player_movement[0] (Up) to get vertical direction
                        self.player.move((self.player_movement[3] - self.player_movement[1], self.player_movement[2] - self.player_movement[0]))

                        # Don't allow player movement until timer has met time limit
                        self.player.can_move = False

                if event.type == pygame.KEYUP:
                    # When keys are released, set player_movement back to false
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player_movement[0] = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player_movement[1] = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player_movement[2] = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player_movement[3] = False
        
            # Recolor the background so it covers everything from the last frame
            self.display.fill((0, 0, 0))

            # Add all of the tiles for the background
            self.tilemap.render(self.display)
            
            # moves the rectangle
            self.mover.move()
    
            # draws the rectangle and color red
            self.mover.draw(self.display, "RED")

            # Draw the player at its current location to the screen
            self.player.render(self.display)
            
            # Blit the screen, display, with all of the sprites on to the screen
            # The display is smaller than the screen so it scales up the size of everything in the display
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            # Updates the display to show all changes made to the game
            pygame.display.update()
            
            # Makes the game run at 60 frames per second
            self.clock.tick(60)

Game().run()
