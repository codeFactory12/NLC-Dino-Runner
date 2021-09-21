import pygame

from nlc_dino_runner.components.powerups.power_up_manager import PowerUpManager
from nlc_dino_runner.utils.constants import RUNNING,ICON
from nlc_dino_runner.components import text_utils
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
        self.points = 0
        self.running = True
        self.death_count = 0
        self.power_up_manager = PowerUpManager()
        # self.Cactus = Cactus(SMALL_CACTUS)
        # self.Cactus = Cactus(LARGE_CACTUS)

    def run(self):
        self.obstacle_manager.reset_obstacles()
        self.power_up_manager.reset_power_ups(self.points)
        self.points = 0
        self.playing = True
        while self.playing:
            self.event()
            self.update()
            self.draw()
        # if pygame.quit():

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        self.power_up_manager.update(self.points, self.game_speed, self.player)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.score()

        pygame.display.update()   #update de pantalla
        pygame.display.flip()  #actualizar la pantalla

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 1
        score_element, score_element_rect = text_utils.get_score_element(self.points)
        self.screen.blit(score_element, score_element_rect)
        self.player.check_invincibility(self.screen)



    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_poss_bg, self.y_poss_bg))

        # La imagen se mueve
        self.screen.blit(BG, (self.x_poss_bg + image_width, self.y_poss_bg))

        # Resetear x = 0
        if self.x_poss_bg <= -image_width:
            self.screen.blit(BG, (self.x_poss_bg + image_width, self.y_poss_bg))
            self.x_poss_bg = 0
        self.x_poss_bg -= self.game_speed

    def execute(self):

        while self.running:
            if not  self.playing:
                self.show_menu()

    def show_menu(self):
        self.running = True
        white_color = (255, 255, 255)
        self.screen.fill(white_color)
        self.print_menu_elements()
        pygame.display.update()
        self.handle_key_events_en_menu()

    def handle_key_events_en_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()

    def print_menu_elements(self):
        half_screen_height = SCREEN_HEIGHT // 2
        text, text_rect = text_utils.get_centered_message("PRESS ANY KEY TO START")
        self.screen.blit(text, text_rect)

        death_score, death_score_rect = text_utils.get_centered_message("DEATH COUNT: ")
        self.screen.blit(death_score, death_score_rect)

        self.screen.blit(RUNNING[0], ((SCREEN_WIDTH // 2) - 40, half_screen_height - 150))
