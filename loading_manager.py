### loading_manager.py
import pygame
from utils import load_and_scale

class LoadingManager:
    def __init__(self, screen):
        self.screen = screen
        self.loading_intro_images = [load_and_scale(f"ASSET/LOADING/load ({i}).png") for i in range(1, 23)]
        self.frame = 0
        self.intro_frame_delay = 1
        self.frame_counter = 0
        self.done = False

    def update(self):
        self.frame_counter += 1
        if self.frame_counter >= self.intro_frame_delay:
            self.frame += 1
            self.frame_counter = 0
            if self.frame >= len(self.loading_intro_images):
                self.done = True
                self.frame = len(self.loading_intro_images) - 1  # Hold last frame

    def draw(self):
        self.screen.blit(self.loading_intro_images[min(self.frame, len(self.loading_intro_images)-1)], (0, 0))

    def is_done(self):
        return self.done
