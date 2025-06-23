### menu_manager.py
import pygame
from utils import load_and_scale

class MenuManager:
    def __init__(self, screen):
        self.screen = screen
        self.menu_images = [load_and_scale(f'ASSET/MENU/menu ({i}).png') for i in range(1, 3)]
        self.play_images = [load_and_scale(f'ASSET/PLAY/play ({i}).png') for i in range(1, 22)]
        self.about_images = [load_and_scale(f'ASSET/ABOUT/about ({i}).png') for i in range(1, 22)]
        self.instruction_images = [load_and_scale(f'ASSET/INSTRUCTIONS/instructions ({i}).png') for i in range(1, 22)]
        self.quit_images = [load_and_scale(f'ASSET/QUIT/quit ({i}).png') for i in range(1, 22)]
        self.options = ["PLAY", "ABOUT", "INSTRUCTION", "QUIT"]
        self.current_option = 0
        self.frame = 0
        self.image_sequence = self.play_images

    def handle_event(self, event, click_sound):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.current_option = (self.current_option + 1) % len(self.options)
                click_sound.play()
                self.update_image_sequence()
            elif event.key == pygame.K_UP:
                self.current_option = (self.current_option - 1) % len(self.options)
                click_sound.play()
                self.update_image_sequence()
            elif event.key == pygame.K_RETURN:
                click_sound.play()
                return self.options[self.current_option]
        return None

    def update_image_sequence(self):
        if self.options[self.current_option] == "PLAY":
            self.image_sequence = self.play_images
        elif self.options[self.current_option] == "ABOUT":
            self.image_sequence = self.about_images
        elif self.options[self.current_option] == "INSTRUCTION":
            self.image_sequence = self.instruction_images
        elif self.options[self.current_option] == "QUIT":
            self.image_sequence = self.quit_images
        self.frame = 0

    def update(self):
        self.frame = (self.frame + 1) % len(self.image_sequence)

    def draw(self):
        self.screen.blit(self.image_sequence[self.frame], (0, 0))
