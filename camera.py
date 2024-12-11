import pygame

class Camera:
    def __init__(self, screen_width, screen_height):
        self.x = 0  # Horizontal position of the camera
        self.y = 0  # Vertical position of the camera
        self.screen_width = screen_width
        self.screen_height = screen_height

    def update(self, player_x, player_y):
        # Center the camera on the player
        self.x = player_x - self.screen_width // 2
        self.y = player_y - self.screen_height // 2

    def apply(self, obj):
        # Adjust an object's position relative to the camera
        return obj.move(-self.x, -self.y)

    # def __init__(self, screen_height):
  
    #    # Initialize the camera with the screen dimensions.
    #     self.y = 0  # Camera's vertical position (offset)
    #     self.screen_height = screen_height

    # def update(self, player_y):
    #    # Update the camera's vertical position to center the player.

    #     self.y = player_y - self.screen_height // 2 
        
    # def apply(self, obj):
    #    # Adjust the object's position relative to the camera.

    #     return obj.move(0, -self.y)
