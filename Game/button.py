from Game.PPlay.sprite import *

class Btn:

    obj = None
    text = None
    gui = None

    def __init__(self, path, txt, window_, x=0, y=0):
        self.obj = Sprite(path)
        self.text = txt
        self.gui = window_
        self.obj.x = x
        self.obj.y = y

    def set_location(self, x, y):
        self.obj.x = x
        self.obj.y = y

    def draw(self):
        self.obj.draw()
        self.gui.draw_text(self.text, self.obj.x, self.obj.y)


