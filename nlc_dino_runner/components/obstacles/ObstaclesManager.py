import pygame.time

from nlc_dino_runner.components.obstacles.Cactus import Cactus
from nlc_dino_runner.utils.constants import SMALL_CACTUS


class ObstaclesManager:

    def __init__(self):
        self.obstacles_list = []

    def update (self, game):

        if len(self.obstacles_list) == 0:
            self.obstacles_list.append(Cactus(SMALL_CACTUS))

        for obstacle in self.obstacles_list:
            obstacle.update(game.game_speed, self.obstacles_list)
            if game.player.dino_rect.colliderect(obstacle.rect):
                if game.player.shield:
                    self.obstacle_list.remove(obstacle)
                else:
                    pygame.time.delay(10000)
                    game.playing = False
                    game.death_count += 1
                    break
            #Rect1.colliderect(Rect2)

    def draw(self, screen):
        for obstacle in self.obstacles_list:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles_list = []