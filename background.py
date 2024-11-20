import pygame

class Background:
    def __init__(self, color, screen_size):
        self.color = color  # Background color
        self.width, self.height = screen_size  # Screen dimensions
        self.camera_offset = 0  # How far the background has scrolled
        self.float_camera_offset = 0.0  # For smoother scrolling
        self.scrolling = False  # Scrolling starts inactive


    def update(self, player_y, threshold, scroll_speed):

        if self.scrolling:
            self.float_camera_offset -= scroll_speed  # Scroll downwards
            self.camera_offset = int(self.float_camera_offset)

            # Stop scrolling when the background reloads
            if abs(self.camera_offset) >= self.height:
                self.camera_offset = 0
                self.float_camera_offset = 0.0
                self.scrolling = False  # Stop scrolling

        # Start scrolling when the player reaches the top
        elif player_y < threshold:
            self.scrolling = True
        """
        Update the camera offset if the player is near the top of the screen.
        """
       # if player_y < threshold:
           # self.camera_offset -= scroll_speed
            # Decrease offset to move background downwards

    def render(self, display):
        """
        Render the scrolling background with wrapping logic.
        """
        # Calculate the y-position for two wrapping backgrounds
        y1 = -self.camera_offset % self.height
        y2 = y1 - self.height

        # Draw the two backgrounds to create the wrapping effect
        pygame.draw.rect(display, self.color, (0, y1, self.width, self.height))
        pygame.draw.rect(display, self.color, (0, y2, self.width, self.height))
