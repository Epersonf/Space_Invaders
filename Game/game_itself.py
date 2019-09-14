
class Game_Itself:

    gui = None
    kbrd = None
    ms = None

    def __init__(self, gui):
        self.gui = gui
        self.kbrd = gui.get_mouse()
        self.ms = gui.get_keyboard()

    def draw(self, level, mode):
        self.gui.set_background_color((0, 0, 0))
