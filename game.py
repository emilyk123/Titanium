
import sys
import pygame
from player import Player
from power import PowerUp

class Game:
    def __init__(self):
        pygame.init()

        screen_width = 640
        screen_height = 480
        # Create game window
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        # Create clock used to limit frame rate
        self.clock = pygame.time.Clock()
        # Create custom events
        self.player_move_event = pygame.USEREVENT + 1
        # [Up, Left, Down, Right]
        self.player_movement = [False, False, False, False]

        # Create player at position 50, 50
        self.player = Player((50, 50))

        # Create power-up with random positioning logic
        self.power = PowerUp(screen_width, screen_height)

    def run(self):
        # Set timer for player movement (every 1 second)
        pygame.time.set_timer(self.player_move_event, 1000)

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

                        # Move the player based on input
                        self.player.move((self.player_movement[3] - self.player_movement[1], self.player_movement[2] - self.player_movement[0]))

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

            # Recolor the background so it covers everything from the last frame
            self.screen.fill((0, 0, 0))

            # Draw the power-up at its current position
            self.power.draw(self.screen)

            # Draw the player at its current location
            self.player.render(self.screen)

            # Updates the display to show all changes made to the game
            pygame.display.update()

            # Makes the game run at 60 frames per second
            self.clock.tick(60)

Game().run()
