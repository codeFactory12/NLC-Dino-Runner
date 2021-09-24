from nlc_dino_runner.components.powerups.powerup import PowerUp
from nlc_dino_runner.utils.constants import HAMMER, HAMMER_TYPE



class HammerPowerUp(PowerUp):

    def __init__(self):
        self.image = HAMMER
        self.type = HAMMER_TYPE
        super().__init__(self.image, self.type)