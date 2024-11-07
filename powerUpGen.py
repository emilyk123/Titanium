# import pygame
# import random

# # Power-up class for speed and invisibility
# class PowerUpGen(pygame.sprite.Sprite):
#     def __init__(self, screen_width, screen_height):
#         super().__init__()
#         self.screen_width = screen_width
#         self.screen_height = screen_height
#         self.width, self.height = 16, 16  # size of the power-up
#         self.image = pygame.Surface((self.width, self.height))
#         self.rect = self.image.get_rect()
        
#         # Randomize initial position and type
#         self.randomize_position()
#         self.type = random.choice(["speed", "invisibility"])
        
#         # Color the power-up based on its type
#         if self.type == "speed":
#             self.image.fill((0, 255, 0))  # Green for speed
#         elif self.type == "invisibility":
#             self.image.fill((0, 0, 255))  # Blue for invisibility

#     def randomize_position(self):
#         # Place the power-up at a random position
#         self.rect.x = random.randint(0, self.screen_width - self.width)
#         self.rect.y = random.randint(0, self.screen_height - self.height)
        
#     def draw(self, surface):
#         surface.blit(self.image, self.rect)
