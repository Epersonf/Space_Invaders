from Game.PPlay.sprite import *

class S_fire:

    obj = None
    gui = None

    def __init__(self, gui, x=-800, y=-800):
        self.obj = Sprite("Assets/S_FIRE.png")
        self.gui = gui
        self.obj.x = x
        self.obj.y = y

    def draw(self):
        self.obj.y -= self.gui.delta_time() * 500
        if self.obj.y > -self.obj.height:
            self.obj.draw()
            return True
        return False
