import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(0, 0, width, height)
        self.alpha = 255
        self.color = (255, 255, 255, 255)
