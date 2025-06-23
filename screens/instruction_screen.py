import pygame
from utils import load_and_scale

class InstructionScreen:
    def __init__(self, screen):
        self.screen = screen
        self.image  = load_and_scale('ASSET/instructions.png')

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            return "menu"
        return None

    def update(self):
        # No dynamic content
        pass

    def draw(self):
        self.screen.blit(self.image, (0, 0))