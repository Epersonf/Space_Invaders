from Game.PPlay.sprite import *

class Ovni:


    obj = None
    vel = 100
    x_vel = vel
    y_vel = 0

    def signal(self, i):
        if i > 0:
            return 1
        elif i < 0:
            return -1
        else:
            return 0

    gui = None

    def __init__(self, path, gui):
        self.obj = Sprite(path)
        self.gui = gui

    def set_location(self, x, y):
        self.obj.x = x
        self.obj.y = y

    def moveX(self, speed=1):
        self.x_vel = speed*self.signal(speed)

    def moveY(self, speed=1):
        self.y_vel = speed*self.signal(speed)

    def draw(self):
        self.obj.x += self.x_vel * self.gui.delta_time()
        self.obj.y += self.y_vel * self.gui.delta_time()
        self.obj.draw()
