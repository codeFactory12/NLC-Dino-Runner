import pygame

from nlc_dino_runner.components.dinosaur import Dinosaur
from nlc_dino_runner.components.obstacles.Cactus import Cactus
from nlc_dino_runner.components.obstacles.ObstaclesManager import ObstaclesManager
from nlc_dino_runner.utils.constants import TITLE, ICON, SCREEN_WIDTH, SCREEN_HEIGHT, BG, FPS, SMALL_CACTUS, \
    LARGE_CACTUS


class Game:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.playing = False
        self.x_poss_bg = 0
        self.y_poss_bg = 360
        self.game_speed = 20
        self.player = Dinosaur()
        self.obstacle_manager = ObstaclesManager()
        # self.Cactus = Cactus(SMALL_CACTUS)
        # self.Cactus = Cactus(LARGE_CACTUS)

    def run(self):
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()
        pygame.quit()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        pygame.display.update()   #update de pantalla
        pygame.display.flip()  #actualizar la pantalla

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_poss_bg, self.y_poss_bg))

        # La imagen se mueve
        self.screen.blit(BG, (self.x_poss_bg + image_width, self.y_poss_bg))

        # Resetear x = 0
        if self.x_poss_bg <= -image_width:
            self.screen.blit(BG,(self.x_poss_bg + image_width, self.y_poss_bg))
            self.x_poss_bg = 0
        self.x_poss_bg -= self.game_speed

