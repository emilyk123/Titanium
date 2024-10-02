import pygame 
from sys import exit
from object import MovingRectangle

#initialize pygame

pygame.init() 

#create a pygame screen 
screen_width = 800
screen_heigth = 400
screen = pygame.display.set_mode((screen_width, screen_heigth))

# create a new clock object 
clock = pygame.time.Clock()

# instance 
mover = MovingRectangle(x=screen_width, y=200, width=500, height=60, speed=-5) 



# game loop


while True:
    for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             exit()

    # set screen color to black
    screen.fill((0, 0, 0))
    
    # moves the rectangle
    mover.move()
    
    # draws the rectangle and color red
    mover.draw(screen, "RED")     
    pygame.display.update()
    clock.tick(60)
