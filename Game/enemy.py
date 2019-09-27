from Game.PPlay.sprite import *

class Enemy:

    obj = None
    gui = None
    x_vel = 50
    y_vel = None
    hit = False

    def __init__(self, gui, path):
        self.obj = Sprite(path)
        self.gui = gui
        self.y_vel = self.obj.height

    def get_hit(self):
        if self.hit:
            self.hit = False
            return not self.hit
        else:
            return self.hit

    def down(self):
        self.obj.y += self.y_vel
        self.x_vel = -self.x_vel
        self.obj.x += self.x_vel *self.gui.delta_time() *5

    def draw(self):

        self.obj.x += self.x_vel * self.gui.delta_time()

        if self.obj.x < 0 or self.obj.x > self.gui.width - self.obj.width:
            self.hit = True

        self.obj.draw()
