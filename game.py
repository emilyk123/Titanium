# Used tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&list=LL&index=5&t=2735s&ab_channel=DaFluffyPotato
# How to create custom events: https://stackoverflow.com/questions/24475718/pygame-custom-event
# How to create a timer: https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer

import sys
import pygame
from player import Player
from tilemap import Tilemap
from object import MovingRectangle
from power import PowerUp
from screen import MainMenu
from screen import PauseMenu
from screen import GameOver
from utils import load_images

from enum import Enum

class CurrentState(Enum):
    MainMenu = 1
    Game = 2
    GameOver = 3
    Pause = 4

class Game:
    def __init__(self):
        pygame.init() 

        self.screen_width = 640
        self.screen_height = 480

        self.display_width = 320
        self.display_height = 240

        self.spawn_position = (self.display_width / 2, self.display_height - 32)

        # Keeps track of which state the player is at in the game
        self.current_state = CurrentState.MainMenu

        self.main_menu = MainMenu(self)
        self.pause_menu = PauseMenu(self)
        self.game_over = GameOver(self)
        
        # Create game window
        self.display = pygame.Surface((self.display_width, self.display_height))

        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # Create clock used to limit frame rate
        self.clock = pygame.time.Clock()
        # Create custom event
        self.player_move_event = pygame.USEREVENT + 1
        self.menu_delay_event = pygame.USEREVENT + 2
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
            'end_tiles': load_images('end_tiles'),
            'water': load_images('water'),
            'health': load_images('health')
        }

        # Keeps track of when the player has pressed the left mouse button
        self.clicked = False

        self.can_click_button = True

        # Try to load level 1, if it's not there then load game without it
        try:
            self.tilemap.load('level01.json')
        except FileNotFoundError:
            pass
    
        # instance 
        self.mover = MovingRectangle(x=self.display_width, y=self.display_height - 80, width=64, height=16, speed=-2) 

    def run(self):
        # Set timer for player movement
        pygame.time.set_timer(self.player_move_event, 100)
        # Set timer to put a delay how fast the player can press menu buttons
        pygame.time.set_timer(self.menu_delay_event, 500)

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
                # Allow the player to click buttons in the menu again
                if event.type == self.menu_delay_event:
                    self.can_click_button = True
                # Check for input with WASD or the arrow keys
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.current_state = CurrentState.Pause
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
                        self.player.move(self.tilemap, (self.player_movement[3] - self.player_movement[1], self.player_movement[2] - self.player_movement[0]), self, self.mover.rect)
                        # Check for collision between player and power-up
                        if self.player.collision(self.power):
                            print("Power-up collected! Moving to a new position.")
                            self.power.randomize_position()
                        # Don't allow player movement until timer has met time limit again
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.clicked = True
                else:
                    self.clicked = False
            

            if not self.player.is_alive:
                self.current_state = CurrentState.GameOver
                self.player.is_alive = True
                self.player.health = 3

            if self.current_state == CurrentState.MainMenu:
                self.display.fill((255, 255, 255))
                self.main_menu.render(self.display)
                if self.clicked and self.main_menu.current_button == "Start" and self.can_click_button:
                    self.current_state = CurrentState.Game
                    self.can_click_button = False
                if self.clicked and self.main_menu.current_button == "Quit":
                    pygame.quit()
                    sys.exit()
            
            elif self.current_state == CurrentState.Pause:
                self.display.fill((255, 255, 255))
                self.pause_menu.render(self.display)
                if self.clicked and self.pause_menu.current_button == "MainMenu" and self.can_click_button:
                    self.current_state = CurrentState.MainMenu
                    self.can_click_button = False
                if self.clicked and self.pause_menu.current_button == "Quit":
                    pygame.quit()
                    sys.exit()
            
            elif self.current_state == CurrentState.GameOver:
                self.display.fill((255, 255, 255))
                self.game_over.render(self.display)
                if self.clicked and self.game_over.current_button == "Restart" and self.can_click_button:
                    self.current_state = CurrentState.Game
                    self.can_click_button = False
                if self.clicked and self.game_over.current_button == "Quit":
                    pygame.quit()
                    sys.exit()
            
            elif self.current_state == CurrentState.Game:
                # Recolor the background so it covers everything from the last frame
                self.display.fill((106, 183, 215))
                # Add all of the tiles for the background
                self.tilemap.render(self.display)
                
                # moves the rectangle
                self.mover.move(self.display_width)
        
                # draws the rectangle and color red
                self.mover.draw(self.display, "RED")
                # if player collides with rectangle move along with the rectangle
                if self.player.rect().colliderect(self.mover.rect):
                    if self.player.rect().bottom <= self.mover.rect.bottom:
                            # move the player with the rectangle speed
                            self.player.position[0] += self.mover.speed
                
                # Draw power-up at random positions
                self.power.draw(self.display)
                # Draw the player at its current location to the screen
                self.player.render(self.display)
                # Draw squares in top right corner to display the player's health
                self.tilemap.draw_health(self.display, self.player)
                
            # Blit the screen, display, with all of the sprites on to the screen
            # The display is smaller than the screen so it scales up the size of everything in the display
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))

            # Updates the display to show all changes made to the game
            pygame.display.update()

            # Makes the game run at 60 frames per second
            self.clock.tick(60)

Game().run()
