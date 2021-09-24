from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import HAMMER


class Hammer(Sprite):

    def __init__(self, RECT_X, RECT_Y):
        Sprite.__init__(self)
        self.image = HAMMER
        self.rect = self.image.get_rect()
        self.rect.x = RECT_X
        self.rect.y = RECT_Y
        self.hammer_speed = 10

    def update(self):
        self.rect.x += self.hammer_speed
        if self.rect.x > self.rect.width:
            self.kill()

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        #CLASE 8 - HAMMER
        #CLASE 8.1 - HAMMER
