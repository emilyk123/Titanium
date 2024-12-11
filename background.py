import pygame

class Background:
    def __init__(self, color, screen_size):
        self.color = color  # Background color
        self.width, self.height = screen_size  # Screen dimensions
        self.camera_offset = 0  # How far the background has scrolled
        self.float_camera_offset = 0.0  # For smoother scrolling
        self.scrolling = False  # Scrolling starts inactive

    def update(self, player_y, threshold, scroll_speed, camera_y):
        
        if self.scrolling:
            self.float_camera_offset -= scroll_speed
            self.camera_offset = int(camera_y)

            if abs(self.camera_offset) >= self.height:
                self.camera_offset = 0
                self.float_camera_offset = 0.0
                self.scrolling = False

        elif player_y < threshold:
            self.scrolling = True

    def render(self, display, camera):
        y1 = -camera.y % self.height
        y2 = y1 - self.height

        # Draw the background as a solid color
        pygame.draw.rect(display, self.color, (0, y1, self.width, self.height))
        pygame.draw.rect(display, self.color, (0, y2, self.width, self.height))
