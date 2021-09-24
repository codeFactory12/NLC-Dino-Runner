from nlc_dino_runner.components.lives.Life import Life

class LivesManager:

    def __init__(self):
        self.lives = 4

    def draw(self, screen):
        pos_x = 50
        for life in range(self.lives):
            heart = Life(pos_x)
            heart.draw(screen)
            pos_x += 30

    def reduce_lives(self):
        self.lives -= 1

    def reset_lives(self):
        self.lives = 4
