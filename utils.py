### utils.py
import pygame

def load_and_scale(path, width=850, height=550):
    return pygame.transform.scale(pygame.image.load(path), (width, height))
