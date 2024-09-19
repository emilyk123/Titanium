# Used tutorial https://www.youtube.com/watch?v=2gABYM5M0ww&list=LL&index=5&t=2735s&ab_channel=DaFluffyPotato

import sys
import pygame

class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            pygame.display.update()
            self.clock.tick(60)

Game().run()