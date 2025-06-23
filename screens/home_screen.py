import pygame
from utils import load_and_scale

class HomeManager:
    def __init__(self, screen):
        self.screen    = screen
        # Load HOME frames
        self.frames    = [load_and_scale(f"ASSET/HOME/HOME ({i}).png") for i in range(1, 6)]
        self.frame_idx = 0
        self.counter   = 0
        self.delay     = 10  # ticks per frame
        self.finished  = False

    def handle_event(self, event):
        # After animation finishes, any key advances to menu
        if self.finished and event.type == pygame.KEYDOWN:
            return "menu"
        return None

    def update(self):
        if not self.finished:
            self.counter += 1
            if self.counter >= self.delay:
                self.counter = 0
                self.frame_idx += 1
                if self.frame_idx >= len(self.frames):
                    # End of animation
                    self.frame_idx = len(self.frames) - 1
                    self.finished  = True

    def draw(self):
        # Draw current frame only
        self.screen.blit(self.frames[self.frame_idx], (0, 0))