from Game.button import *


class Mode_Gui:

    gui = None
    kbrd = None
    ms = None
    Easy = None
    Medium = None
    Hard = None

    def __init__(self, gui):
        self.gui = gui
        self.kbrd = gui.get_mouse()
        self.ms = gui.get_keyboard()
        self.Easy = Btn("Assets/BTN.png", "Easy", gui, gui.width / 2 - 200, 0)
        self.Medium = Btn("Assets/BTN.png", "Medium", gui, gui.width / 2 - 200, 100)
        self.Hard = Btn("Assets/BTN.png", "Hard", gui, gui.width / 2 - 200, 200)

    def draw(self, level, mode):
        self.gui.set_background_color((0, 0, 0))
        if self.Easy.draw():
            level[0] = 3
            mode[0] = 1
        if self.Medium.draw():
            level[0] = 3
            mode[0] = 2
        if self.Hard.draw():
            level[0] = 3
            mode[0] = 3
