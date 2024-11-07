# https://pygame.readthedocs.io/en/latest/4_text/text.html (How to put text on the screen)
# https://www.geeksforgeeks.org/mmouse-clicks-on-sprites-in-pygame/# (How to know when the mouse is hovering over a rect)

import pygame

# Since display is half the size of screen, this is used to adjust the position from the screen size to the display size
RENDER_SCALE = 2.0

class MainMenu:
    def __init__(self, game):
        self.game = game
        self.mpos = pygame.mouse.get_pos()
        self.current_button = None
    
    def render(self, surface):
        font = pygame.font.SysFont('Consolas', 24)
        img = font.render('Main Menu', True, pygame.Color(0, 0, 0))
        surface.blit(img, ((self.game.display_width // 2) - (img.get_width() // 2), self.game.display_height // 3))

        self.mpos = pygame.mouse.get_pos()
        self.mpos = (self.mpos[0] / RENDER_SCALE, self.mpos[1] / RENDER_SCALE)

        start_button = Button(20, 60, ((self.game.display_width // 5), self.game.display_height // 2), 'Start')
        start_button_rect = pygame.Rect(start_button.position[0], start_button.position[1], start_button.length * RENDER_SCALE, start_button.width * RENDER_SCALE)

        quit_button = Button(20, 60, ((self.game.display_width // 1.7), self.game.display_height // 2), 'Quit')
        quit_button_rect = pygame.Rect(quit_button.position[0], quit_button.position[1], quit_button.length * RENDER_SCALE, quit_button.width * RENDER_SCALE)

        if start_button_rect.collidepoint(self.mpos):
            self.current_button = "Start"
        elif quit_button_rect.collidepoint(self.mpos):
            self.current_button = "Quit"
        else:
            self.current_button = None

        start_button.render(surface)
        quit_button.render(surface)

class PauseMenu:
    def __init__(self, game):
        self.game = game
        self.mpos = pygame.mouse.get_pos()
        self.current_button = None
    
    def render(self, surface):
        font = pygame.font.SysFont('Consolas', 24)
        img = font.render('Pause Menu', True, pygame.Color(0, 0, 0))
        surface.blit(img, ((self.game.display_width // 2) - (img.get_width() // 2), self.game.display_height // 3))

        self.mpos = pygame.mouse.get_pos()
        self.mpos = (self.mpos[0] / RENDER_SCALE, self.mpos[1] / RENDER_SCALE)

        main_menu_button = Button(20, 100, ((self.game.display_width // 5), self.game.display_height // 2), 'Main Menu')
        main_menu_button_rect = pygame.Rect(main_menu_button.position[0], main_menu_button.position[1], main_menu_button.length * RENDER_SCALE, main_menu_button.width * RENDER_SCALE)

        quit_button = Button(20, 60, ((self.game.display_width // 1.7), self.game.display_height // 2), 'Quit')
        quit_button_rect = pygame.Rect(quit_button.position[0], quit_button.position[1], quit_button.length * RENDER_SCALE, quit_button.width * RENDER_SCALE)

        if main_menu_button_rect.collidepoint(self.mpos):
            self.current_button = "MainMenu"
        elif quit_button_rect.collidepoint(self.mpos):
            self.current_button = "Quit"
        else:
            self.current_button = None

        main_menu_button.render(surface)
        quit_button.render(surface)

class GameOver:
    def __init__(self, game):
        self.game = game
        self.mpos = pygame.mouse.get_pos()
        self.current_button = None
    
    def render(self, surface):
        font = pygame.font.SysFont('Consolas', 24)
        img = font.render('Game Over!', True, pygame.Color(0, 0, 0))
        surface.blit(img, ((self.game.display_width // 2) - (img.get_width() // 2), self.game.display_height // 3))

        self.mpos = pygame.mouse.get_pos()
        self.mpos = (self.mpos[0] / RENDER_SCALE, self.mpos[1] / RENDER_SCALE)

        main_menu_button = Button(20, 80, ((self.game.display_width // 5), self.game.display_height // 2), 'Restart')
        main_menu_button_rect = pygame.Rect(main_menu_button.position[0], main_menu_button.position[1], main_menu_button.length * RENDER_SCALE, main_menu_button.width * RENDER_SCALE)

        quit_button = Button(20, 60, ((self.game.display_width // 1.7), self.game.display_height // 2), 'Quit')
        quit_button_rect = pygame.Rect(quit_button.position[0], quit_button.position[1], quit_button.length * RENDER_SCALE, quit_button.width * RENDER_SCALE)

        if main_menu_button_rect.collidepoint(self.mpos):
            self.current_button = "Restart"
        elif quit_button_rect.collidepoint(self.mpos):
            self.current_button = "Quit"
        else:
            self.current_button = None

        main_menu_button.render(surface)
        quit_button.render(surface)

class Button:
    def __init__(self, length, width, position, text):
        self.length = length
        self.width = width
        self.position = list(position)

        font = pygame.font.SysFont('Consolas', 20)
        self.img = font.render(text, True, pygame.Color(0, 0, 0))
    
    def render(self, surface):
        pygame.draw.rect(surface, pygame.Color(0, 255, 0), pygame.Rect(self.position[0], self.position[1], self.width, self.length))
        surface.blit(self.img, (self.position[0], self.position[1]))