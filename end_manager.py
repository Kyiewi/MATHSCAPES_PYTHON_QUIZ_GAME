import pygame
from utils import load_and_scale

class EndManager:
    def __init__(self, screen, end_sound):
        self.screen = screen
        self.end_sound = end_sound

        self.won_images = [load_and_scale(f'ASSET/WON/WON ({i}).png') for i in range(1, 22)]
        self.end_intro_images = [load_and_scale(f'ASSET/END/END ({i}).png') for i in range(1, 3)]
        self.ending_loop_images = [load_and_scale(f'ASSET/END/end ({i}).png') for i in range(1, 21)]

        self.state = 'won'         # 'won' -> 'intro' -> 'loop'
        self.frame = 0
        self.frame_counter = 0

        # You can tweak these values for animation smoothness
        self.won_delay = 3          # frames per image (3 = ~50ms)
        self.intro_delay = 20       # long pause between 2 intro frames
        self.loop_delay = 2         # shorter = faster looping

        self.sound_played = False

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                return "level"
            elif event.key == pygame.K_b:
                return "menu"
        return None

    def update(self):
        self.frame_counter += 1

        if self.state == 'won':
            if not self.sound_played:
                self.end_sound.play()
                self.sound_played = True
            if self.frame_counter >= self.won_delay:
                self.frame_counter = 0
                self.frame += 1
                if self.frame >= len(self.won_images):
                    self.state = 'intro'
                    self.frame = 0

        elif self.state == 'intro':
            if self.frame_counter >= self.intro_delay:
                self.frame_counter = 0
                self.frame += 1
                if self.frame >= len(self.end_intro_images):
                    self.state = 'loop'
                    self.frame = 0

        elif self.state == 'loop':
            if self.frame_counter >= self.loop_delay:
                self.frame_counter = 0
                self.frame = (self.frame + 1) % len(self.ending_loop_images)

    def draw(self):
        if self.state == 'won':
            img = self.won_images[min(self.frame, len(self.won_images) - 1)]
        elif self.state == 'intro':
            img = self.end_intro_images[min(self.frame, len(self.end_intro_images) - 1)]
        else:  # loop
            img = self.ending_loop_images[self.frame]
        self.screen.blit(img, (0, 0))
