# import pygame 
# import random 



# # powerup class for speed and invisibility 

# class PowerUpGeneral(pygame.sprite.Sprite):
#     def __init__(self, x, y, power_type):
#         super().__init__()
#         # creating the size of the powerup
#         self.image() = pygame.Surface((20,20))
#         self.rect = self.image.get_rect(center = (x,y))
#         self.power_type = power_type
#         self.active 

#         # setting attributes based on the power up type 

#         if self.power_type == "speed":
#             self.image.fill((0, 225, 0)) # green for speed 
#             # duration speed of 5 seconds 
#             self.duration = 500 
#         # powerup for invisibility 
#         elif self.power_type == "invisibility":
#             self.image.fill((0,0,255)) # blue for invisibility 
#             # duration speed of 3 seconds 
#             self.duration = 3000

#     # activate the power up on player 
#     def activate(self, player):
#         self.activate = True
#         self.start_time = pygame.time.get_ticks()


#         # apply power up type to the player 
#         if self.power_type == "speed":
#             player.speed += 5 # increase player speed 
#         elif self.power_type == "invisibility":
#             player.invisible == True 

#     def update(self, player):
#         if self.active:
#             current_time = pygame.time.get_ticks()
#             if current_time - self.start_time >= self.duration:
#                 self.deactivate(player)


#     def deactivate(self, player):
#         self.active = False 

#         # reomove powerup effects 
#         if self.power_type == "speed":
#             player.speed -= 5 # reset speed 
#         elif self.power_type == "invisibility": 
#             player.invsible = False
   





      