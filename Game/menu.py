from Game import stars_ambient
from Game.button import *
from Game.stars_ambient import *

class Main_Menu:

    gui = None
    Play = None
    Mode = None
    Ranking = None
    Exit = None
    Stars_Amb = None

    def __init__(self, gui):
        self.gui = gui
        self.Play = Btn("Assets/BTN.png", "Play", gui, gui.width / 2 - 200, gui.height / 2)
        self.Mode = Btn("Assets/BTN.png", "Mode", gui, gui.width / 2 - 200, gui.height / 2 + 100)
        self.Ranking = Btn("Assets/BTN.png", "Rank", gui, gui.width / 2 - 200, gui.height / 2 + 200)
        self.Exit = Btn("Assets/BTN.png", "Exit", gui, gui.width / 2 - 200, gui.height / 2 + 300)
        self.Stars_Amb = Stars(gui)


    def draw(self, level, mode):
        self.gui.set_background_color((0, 0, 0))
        #self.Stars_Amb.draw()
        if self.Play.draw():
            level[0] = 3
        if self.Mode.draw():
            level[0] = 1
        if self.Ranking.draw():
            level[0] = 2
        if self.Exit.draw():
            exit(0)
