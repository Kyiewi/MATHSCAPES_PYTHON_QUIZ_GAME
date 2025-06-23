### main.py
import sys
import pygame
from game_manager import GameManager

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 850, 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("MATHSCAPES")

pygame.mixer.music.load("SOUNDS/background.mp3")
pygame.mixer.music.play(-1)

click_sound = pygame.mixer.Sound("SOUNDS/click.mp3")
correct_sound = pygame.mixer.Sound("SOUNDS/correct.mp3")
wrong_sound = pygame.mixer.Sound("SOUNDS/wrong.mp3")
end_sound = pygame.mixer.Sound("SOUNDS/end.mp3")

clock = pygame.time.Clock()
game_manager = GameManager(screen, click_sound, correct_sound, wrong_sound, end_sound)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            game_manager.handle_event(event)

    game_manager.update()
    game_manager.draw()
    pygame.display.flip()
    clock.tick(12)

pygame.quit()
sys.exit()
