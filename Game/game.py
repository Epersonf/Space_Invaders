from Game.PPlay.window import *
from Game.menu import *
from Game.game_itself import *
from Game.mode import *

gui = Window(1024, 768)
gui.set_title("Invaders")

#0 = menu, 1 = mode select, 2 = ranking, 3 = game itself
level = [0]

#levels
mm = Main_Menu(gui)
gm = Game_Itself(gui)
mg = Mode_Gui(gui)

#easy = 1, medium = 2, hard = 3
mode = [1]

kbrd = gui.get_keyboard()
ms = gui.get_mouse()

while True:
    if level[0] == 0:
        mm.draw(level, mode)
    elif level[0] == 3:
        gm.draw(level, mode)
    elif level[0] == 1:
        mg.draw(level, mode)

    if kbrd.key_pressed("ESC"):
        level[0] = 0
    gui.update()
