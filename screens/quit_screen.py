import sys
import pygame
from utils import load_and_scale

class QuitManager:
    def __init__(self, screen):
        self.screen = screen
        self.image  = load_and_scale('ASSET/exit.png')

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                pygame.quit()
                sys.exit()
            elif event.key == pygame.K_n:
                return "menu"
        return None

    def update(self):
        # No dynamic content
        pass

    def draw(self):
        self.screen.blit(self.image, (0, 0))