import sys
import pygame
from utils import load_and_scale
from home_screen               import HomeManager
from menu_manager              import MenuManager
from level_manager             import LevelManager
from easy_quiz_manager         import EasyQuizManager
from moderate_quiz_manager     import ModerateQuizManager
from hard_quiz_manager         import HardQuizManager
from about_screen      import AboutScreen
from instruction_screen import InstructionScreen
from quit_screen       import QuitManager
from end_manager               import EndManager
from loading_manager           import LoadingManager

class GameManager:
    def __init__(self, screen, click_sound, correct_sound, wrong_sound, end_sound):
        self.screen        = screen
        self.click_sound   = click_sound
        self.correct_sound = correct_sound
        self.wrong_sound   = wrong_sound
        self.end_sound     = end_sound

        # Initialize all managers
        self.home        = HomeManager(screen)
        self.menu        = MenuManager(screen)
        self.level       = LevelManager(screen)
        self.loading     = None
        self.quiz        = None
        self.end         = EndManager(screen, end_sound)
        self.about       = AboutScreen(screen)
        self.instruction = InstructionScreen(screen)
        self.quit_screen = QuitManager(screen)

        # Start at home
        self.state = "home"

    def handle_event(self, event):
        if self.state == "home":
            result = self.home.handle_event(event)
            if result == "menu":
                self.state = "menu"
            return

        if self.state == "menu":
            result = self.menu.handle_event(event, self.click_sound)
            if result == "PLAY":
                self.state = "level"
            elif result == "ABOUT":
                self.state = "about"
            elif result == "INSTRUCTION":
                self.state = "instruction"
            elif result == "QUIT":
                self.state = "quit"
            return

        if self.state == "level":
            result = self.level.handle_event(event)
            if result in ("easy_quiz", "moderate_quiz", "hard_quiz"):
                self.loading = LoadingManager(self.screen)
                self.state   = "loading"
                self.next_quiz_state = result
            return

        if self.state in ("easy_quiz", "moderate_quiz", "hard_quiz"):
            self.quiz.handle_event(event)
            return

        if self.state == "end":
            result = self.end.handle_event(event)
            if result == "level":
                self.level = LevelManager(self.screen)
                self.state = "level"
            elif result == "menu":
                self.menu  = MenuManager(self.screen)
                self.state = "menu"
            return

        if self.state == "about":
            result = self.about.handle_event(event)
            if result == "menu":
                self.state = "menu"
            return

        if self.state == "instruction":
            result = self.instruction.handle_event(event)
            if result == "menu":
                self.state = "menu"
            return

        if self.state == "quit":
            result = self.quit_screen.handle_event(event)
            if result == "menu":
                self.state = "menu"
            return

    def update(self):
        if self.state == "home":
            self.home.update()
            return

        if self.state == "menu":
            self.menu.update()
            return

        if self.state == "level":
            self.level.update()
            return

        if self.state == "loading":
            self.loading.update()
            if self.loading.is_done():
                if self.next_quiz_state == "easy_quiz":
                    self.quiz = EasyQuizManager(self.screen, self.correct_sound, self.wrong_sound)
                elif self.next_quiz_state == "moderate_quiz":
                    self.quiz = ModerateQuizManager(self.screen, self.correct_sound, self.wrong_sound)
                elif self.next_quiz_state == "hard_quiz":
                    self.quiz = HardQuizManager(self.screen, self.correct_sound, self.wrong_sound)
                self.state = self.next_quiz_state
            return

        if self.state in ("easy_quiz", "moderate_quiz", "hard_quiz"):
            result = self.quiz.update()
            if result == "end":
                self.state = "end"
            return

        if self.state == "end":
            self.end.update()
            return

        if self.state == "about":
            self.about.update()
            return

        if self.state == "instruction":
            self.instruction.update()
            return

        if self.state == "quit":
            self.quit_screen.update()
            return

    def draw(self):
        if self.state == "home":
            self.home.draw()
            return

        if self.state == "menu":
            self.menu.draw()
            return

        if self.state == "level":
            self.level.draw()
            return

        if self.state == "loading":
            self.loading.draw()
            return

        if self.state in ("easy_quiz", "moderate_quiz", "hard_quiz"):
            self.quiz.draw()
            return

        if self.state == "end":
            self.end.draw()
            return

        if self.state == "about":
            self.about.draw()
            return

        if self.state == "instruction":
            self.instruction.draw()
            return

        if self.state == "quit":
            self.quit_screen.draw()
            return
