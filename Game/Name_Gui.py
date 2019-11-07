from Game.name_input import *
from Game.button import *

class Name_Gui:


    inputs = None
    gui = None
    btn = None
    mouse = None

    def __init__(self, gui):
        self.gui = gui
        self.inputs = []
        self.btn = Btn("Assets/BTN.png", "Ok!", gui, 500, 500)
        self.btn.set_location(gui.width/2 - self.btn.obj.width/2, 270)
        self.mouse = gui.get_mouse()
        first_x = 200
        first_y = 200
        for i in range(8):
            n = name_input(gui, first_x, first_y, "_", 40)
            first_x += n.size + 40
            self.inputs.append(n)

    def draw(self, level, name):
        self.gui.set_background_color((0, 0, 0))
        self.gui.draw_text("Type your name:", 300, 100, 40, (255, 255, 255))
        self.btn.draw()
        n = ""
        for i in self.inputs:
            i.draw()
            if i.letter != "_":
                n += i.letter
        if self.btn.mouse_over() and self.mouse.is_button_pressed(1):
            level[0] = 0
            name[0] = n
