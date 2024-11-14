import sys
import pygame
import random
from player import Player
from tilemap import Tilemap
from object import MovingRectangle
from power import PowerUp
from utils import load_images

# olas import 
from powerUpSpeed import SpeedPowerUP 
from powerUpInvisble import InvisblePowerUp

class Game:
    def __init__(self):
        pygame.init() 

        self.screen_width = 640
        self.screen_height = 480

        self.display_width = 320
        self.display_height = 240

        self.spawn_position = (self.display_width / 2, self.display_height - 16)
        
        # Create game window
        self.display = pygame.Surface((self.display_width, self.display_height))

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # Create clock used to limit frame rate
        self.clock = pygame.time.Clock()
        # Create custom event
        self.player_move_event = pygame.USEREVENT + 1
        # [Up, Left, Down, Right]
        self.player_movement = [False, False, False, False]

        # Create player player at spawn position
        self.player = Player(self.spawn_position)
        
        # Create power-up with random positioning logic
        self.power = PowerUp(self.display_width, self.display_height)

        # Initialize the tilemap
        self.tilemap = Tilemap(self)

        # Game Tile Sprites
        self.assets = {
            'ground': load_images('ground'),
            'water': load_images('water'),
            'health': load_images('health')
        }

        # Try to load level 1, if it's not there then load game without it
        try:
            self.tilemap.load('level01.json')
        except FileNotFoundError:
            pass

        # Creating the powerup instances here
        x, y = 100, 100  # Example initial positions for power-ups
        self.invisble_powerUp = InvisblePowerUp(100,100)
        self.speed_powerUp = SpeedPowerUP(200,150)

        self.player_movement_delay = 100
    
        # Create the moving rectangle instance
        self.mover = MovingRectangle(x=self.display_width, y=64, width=64, height=16, speed=-2) 

    def run(self):
        # Set timer for player movement)
        pygame.time.set_timer(self.player_move_event, self.player_movement_delay)

        while True:
            # Checks all key and mouse presses
            for event in pygame.event.get():
                # Pressing the red x at the corner of the window closes the game
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
                        self.player.move(self.tilemap, (self.player_movement[3] - self.player_movement[1], self.player_movement[2] - self.player_movement[0]), self)

                        # Check for collision between player and power-up

                        # if self.player.collision(self.power):
                        #     print("Power-up collected! Moving to a new position.")
                        #     self.power.randomize_position()

                        # # Don't allow player movement until timer has met time limit again
                        # self.player.can_move = False

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
            
            # Move the rectangle
            self.mover.move(self.display_width)
    
            # Draw the rectangle and color it red
            self.mover.draw(self.display, "RED")

            # If player collides with rectangle, move along with the rectangle
            if self.player.rect().colliderect(self.mover.rect):
                if self.player.rect().bottom <= self.mover.rect.bottom:
                    # Move the player with the rectangle speed
                    self.player.position[0] += self.mover.speed
            
            # Draw power-ups at their positions
            self.invisble_powerUp.draw(self.display)
            self.speed_powerUp.draw(self.display)

            # Check for collision with power-ups
            if self.player.rect().colliderect(self.invisble_powerUp.rect):
                # print("Invisible Power-Up collected!")
                self.invisble_powerUp.randomize_position(self.display_width, self.display_height)
            if self.player.rect().colliderect(self.speed_powerUp.rect):
                # print("Speed Power-Up collected!")
                self.speed_powerUp.randomize_position(self.display_width, self.display_height)

                # using player movement delay here
                self.speed_powerUp.speed_up(self)

            # Draw the player at its current location to the screen
            self.player.render(self.display)

            # Draw squares in top right corner to display the player's health
            self.tilemap.draw_health(self.display, self.player)
            
            # Blit the screen, display, with all of the sprites onto the screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            # Updates the display to show all changes made to the game
            pygame.display.update()

            # Makes the game run at 60 frames per second
            self.clock.tick(60)

Game().run()
