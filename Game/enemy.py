from Game.PPlay.sprite import *

class enemy:

    obj = None
    gui = None
    x_vel = 200
    y_vel = 400

    def __init__(self, gui, path):
        self.obj = Sprite(path)
        self.gui = gui

    def draw(self):

        self.obj.x += self.x_vel * self.gui.delta_time()

        if self.obj.x < self.obj.width/2:
            self.obj.x = self.obj.width/2
            self.x_vel = -self.x_vel
            self.obj.y += self.obj.y_vel

        if self.obj.x > self.gui.width - self.obj.width/2:
            self.obj.x = self.gui.width - self.obj.width/2
            self.x_vel = -self.x_vel
            self.obj.y += self.obj.y_vel

        self.obj.draw()
