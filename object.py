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

    def draw(self, screen, color, camera):
         # draws rec on screen
        pygame.draw.rect(screen, color, self.rect)

    # def draw(self, screen, color, camera):
    #     adjusted_rect = self.rect.move(-camera.x, -camera.y)
    #     pygame.draw.rect(screen, color, adjusted_rect)

    
