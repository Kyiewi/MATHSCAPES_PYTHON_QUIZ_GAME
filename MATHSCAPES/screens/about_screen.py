import pygame
from utils import load_and_scale

class AboutScreen:
    def __init__(self, screen):
        self.screen = screen
        self.image  = load_and_scale('ASSET/about.png')

    def handle_event(self, event):
        # Return to menu on any key press
        if event.type == pygame.KEYDOWN:
            return "menu"
        return None

    def update(self):
        # Nothing dynamic to update
        pass

    def draw(self):
        self.screen.blit(self.image, (0, 0))
