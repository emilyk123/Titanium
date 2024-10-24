import sys
import pygame
from player import Player
from object import MovingRectangle

class Game:
    def __init__(self):
        pygame.init()

        screen_width = 640
        screen_height = 480
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()

        self.player_move_event = pygame.USEREVENT + 1
        self.player_movement = [False, False, False, False]

        # Create the player position  50, 50
        self.player = Player((50, 50))

        # instance
        self.mover = MovingRectangle(x=screen_width, y=200, width=500, height=60, speed=-5)

    def run(self):
        pygame.time.set_timer(self.player_move_event, 1000)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == self.player_move_event:
                    self.player.can_move = True

                if event.type == pygame.KEYDOWN:
                    if self.player.can_move:
                        if event.key == pygame.K_w or event.key == pygame.K_UP:
                            self.player_movement[0] = True
                        if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                            self.player_movement[1] = True
                        if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                            self.player_movement[2] = True
                        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                            self.player_movement[3] = True

                        self.player.move((self.player_movement[3] - self.player_movement[1], self.player_movement[2] - self.player_movement[0]))
                        self.player.can_move = False

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.player_movement[0] = False
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.player_movement[1] = False
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.player_movement[2] = False
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.player_movement[3] = False

            self.screen.fill((0, 0, 0))
            self.mover.move()
            self.mover.draw(self.screen, "RED")

            # Checks for collision between players and the rectangle objectl
            if self.player.rect.colliderect(self.mover.rect):
                # if the player is on top of the rectangle move the player
                if self.player.rect.bottom <= self.mover.rect.bottom:
                    # move player with rectangle speed
                    self.player.rect.x += self.mover.speed
                    self.player.position[0] = self.player.rect.x

            self.player.render(self.screen)

            pygame.display.update()
            self.clock.tick(60)

Game().run()
