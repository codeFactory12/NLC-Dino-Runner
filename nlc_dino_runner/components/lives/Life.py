from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HEART


class Life(Sprite):

    def __init__(self, pos_x=50):
        self.image = HEART
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = 30

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))