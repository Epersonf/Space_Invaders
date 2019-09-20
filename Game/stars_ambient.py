from Game.PPlay.gameimage import *
from random import randint

class Stars:

    gui = None
    stars_obj = None
    vel = None

    def __init__(self, gui, amount=2000):
        self.gui = gui
        self.stars_obj = [None] * amount
        self.vel = [None] * amount
        for i in range(amount):
            self.stars_obj[i] = GameImage("Assets/STAR.png")
            self.stars_obj[i].x = randint(0, self.gui.width)
            self.stars_obj[i].y = randint(0, self.gui.height)
            self.vel[i] = randint(0, 300)

    def draw(self):
        for i in range(len(self.stars_obj)):
            self.stars_obj[i].y -= self.vel[i] * self.gui.delta_time()
            if self.stars_obj[i].y <= 0:
                self.stars_obj[i].x = randint(0, self.gui.width)
                self.stars_obj[i].y = self.gui.height
                self.vel[i] = randint(20, 300)
            self.stars_obj[i].draw()
