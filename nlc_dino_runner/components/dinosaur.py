import pygame
from pygame.sprite import Sprite
from nlc_dino_runner.utils.constants import (
    RUNNING,
    DUCKING,
    JUMPING,
    RUNNING_SHIELD,
    DUCKING_SHIELD,
    JUMPING_SHIELD,
    DEFAULT_TYPE,
    SHIELD_TYPE
    )
from nlc_dino_runner.components.text_utils import get_centered_message
class Dinosaur(Sprite):

    #constantes
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 8.5

    def __init__(self):
        self.run_img = {
                        DEFAULT_TYPE: RUNNING,
                        SHIELD_TYPE: RUNNING_SHIELD,
                        }
        self.jum_img = {
                        DEFAULT_TYPE: JUMPING,
                        SHIELD_TYPE: JUMPING_SHIELD,
                        }
        self.duck_img = {
                        DEFAULT_TYPE: DUCKING,
                        SHIELD_TYPE: DUCKING_SHIELD,
                        }
        self.type = DEFAULT_TYPE
        self.image = self.run_img[self.type][0]
        #SHIELD
        self.shield_time_up = 0
        self.shield = False
        self.show_text = False

        self. dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index = 0
        self.dino_run = True
        self.dino_duck = False
        self.dino_jump = False
        self.jump_vel = self.JUMP_VEL

    def event(self):
        pass

    def update(self, user_input):

        if self.dino_jump:
            self.jump()

        if self.dino_duck:
            self.duck()

        if self.dino_run:
            self.run()
        # cuando se agache no pueda saltar

        if user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_jump = False
            self.dino_run = False

        # cuando salte no pueda agacharse
        elif user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_jump = True
            self.dino_duck = False
            self.dino_run = False

        elif not self.dino_jump:
            self.dino_run = True
            self.dino_duck = False
            self.dino_jump = False

        if self.step_index >= 10:
            self.step_index = 0

    def run(self):
        self.image = self.run_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS
        self.step_index += 1

    def duck(self):
        self.image = self.duck_img[self.type][self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.X_POS
        self.dino_rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def jump(self):
        self.image = self.jum_img[self.type]
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 7
            self.jump_vel -= 1

        if self.jump_vel < - self.JUMP_VEL:
            self.dino_rect.y = self.Y_POS
            self.dino_jump = False
            self.jump_vel = self.JUMP_VEL

    def check_invincibility(self, screen):
        if self.shield:
            time_to_show = round((self.shield_time_up - pygame.time.get_ticks())/ 1000, 3)
            if time_to_show < 0:
                self.shield = False
                if self.type == SHIELD_TYPE:
                    self.type = DEFAULT_TYPE

                else:
                    if self.show_text:
                        text, text_rect = get_centered_message(
                            f'Shield enable for {time_to_show}',
                            width=500,
                            height=40,
                            size=20
                        )
                        screen.blit(text, text_rect)
    def draw(self, screen):
        screen.blit(self.image, (self.dino_rect.x, self.dino_rect.y))