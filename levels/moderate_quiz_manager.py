import pygame
from utils import load_and_scale

class ModerateQuizManager:
    def __init__(self, screen, correct_sound, wrong_sound):
        self.screen = screen
        self.correct_sound = correct_sound
        self.wrong_sound = wrong_sound
        self.questions = [load_and_scale(f"ASSET/MODERATE/MODERATE ({i}).png") for i in range(1, 6)]
        self.answers = ["A", "C", "D", "A", "B"]
        self.current_question = 0
        self.feedback_image = None
        self.feedback_timer = 0
        self.correct_image = load_and_scale("ASSET/correct.png")
        self.wrong_image = load_and_scale("ASSET/wrong.png")
        self.advance_to_next = False
        self.finished = False

    def handle_event(self, event):
        if self.feedback_image or self.finished:
            return
        if event.type == pygame.KEYDOWN:
            key = pygame.key.name(event.key).upper()
            if key in ("A", "B", "C", "D"):
                if key == self.answers[self.current_question]:
                    self.feedback_image = self.correct_image
                    self.correct_sound.play()
                    self.advance_to_next = True
                else:
                    self.feedback_image = self.wrong_image
                    self.wrong_sound.play()
                    self.advance_to_next = False
                self.feedback_timer = 12

    def update(self):
        if self.feedback_image:
            self.feedback_timer -= 1
            if self.feedback_timer <= 0:
                self.feedback_image = None

                if self.advance_to_next:
                    self.current_question += 1
                    if self.current_question >= len(self.questions):
                        self.finished = True

        if self.finished:
            return "end"
        return None

    def draw(self):
        if self.feedback_image:
            self.screen.blit(self.feedback_image, (0, 0))
        elif self.current_question < len(self.questions):
            self.screen.blit(self.questions[self.current_question], (0, 0))
