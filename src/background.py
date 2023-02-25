import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.rect = pygame.Rect(0, 0, width, height)
        self.alpha = 255
        self.color = (255, 255, 255, 255)
        self.fadein = False

    def update(self):
        """ Set animation state and opacity
            returns: N/A
        """
        if self.fadein:
            if self.alpha <= 5:
                self.alpha = 0
                self.image.set_alpha(self.alpha)
                self.fadein = False
                return
            self.alpha -= 5
            self.image.set_alpha(self.alpha)

    def draw(self, surface):
        surface.blit(self.image, self.rect)
