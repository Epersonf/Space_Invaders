from Game.PPlay.window import *
from Game.menu import draw_m
from Game.button import *

gui = Window(1024, 768)
gui.set_title("Invaders")

#0 = menu, 1 = mode select, 2 = ranking, 3 = game itself
level = 0

#easy = 1, medium = 2, hard = 3
mode = 1

kbrd = gui.get_keyboard()
ms = gui.get_mouse()

while True:
    if level == 0:
        draw_m()
    gui.update()
