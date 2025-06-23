import pygame
from utils import load_and_scale

class LevelManager:
    def __init__(self, screen):
        self.screen = screen
        self.level_intro_images = [load_and_scale(f"ASSET/LEVEL/LEVEL ({i}).png") for i in range(1, 5)]
        self.level_loop_images  = [load_and_scale(f"ASSET/LEVELS/level ({i}).png") for i in range(1, 22)]
        self.intro_done = False
        self.frame = 0
        self.intro_frame_delay = 10
        self.loop_frame_delay  = 1
        self.frame_counter = 0

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            key_name = pygame.key.name(event.key)
            print(f"[LevelManager] KeyDown: {key_name}")
            if event.key == pygame.K_e:
                print("[LevelManager] → easy_quiz")
                return "easy_quiz"
            elif event.key == pygame.K_m:
                print("[LevelManager] → moderate_quiz")
                return "moderate_quiz"
            elif event.key == pygame.K_h:
                print("[LevelManager] → hard_quiz")
                return "hard_quiz"
        return None

    def update(self):
        self.frame_counter += 1
        if not self.intro_done:
            if self.frame_counter >= self.intro_frame_delay:
                self.frame += 1
                self.frame_counter = 0
                if self.frame >= len(self.level_intro_images):
                    self.intro_done = True
                    self.frame = 0
        else:
            if self.frame_counter >= self.loop_frame_delay:
                self.frame = (self.frame + 1) % len(self.level_loop_images)
                self.frame_counter = 0

    def draw(self):
        if not self.intro_done:
            img = self.level_intro_images[min(self.frame, len(self.level_intro_images)-1)]
        else:
            img = self.level_loop_images[self.frame]
        self.screen.blit(img, (0, 0))
