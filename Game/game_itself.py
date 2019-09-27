from Game.ship import *
from Game.enemy import *
from Game.stars_ambient import *

class Game_Itself:

    gui = None
    kbrd = None
    ms = None
    char = None
    stars = None
    enemies = []

    def __init__(self, gui):
        self.gui = gui
        self.kbrd = gui.get_mouse()
        self.ms = gui.get_keyboard()
        self.char = Nave(gui, "Assets/NAVE.png")
        self.char.set_loc(gui.width // 2 - self.char.obj.width//2, gui.height - 100)
        self.stars = Stars(gui, 100)

    def draw(self, level, mode):
        self.gui.set_background_color((0, 0, 0))
        self.stars.draw()
        self.char.draw(mode)

