import pygame 



# create a rectangle class 

class MovingRectangle:
    def __init__(self, x, y, width, height, speed):

        self.speed = speed
        self.rect = pygame.Rect(x, y, width, height)

    def move(self, width):
        self.rect.x += self.speed

        if self.rect.right < 0: 
            self.rect.x = width

    def draw(self, screen, color):
        # draws rec on screen
        pygame.draw.rect(screen, color, self.rect)
    
