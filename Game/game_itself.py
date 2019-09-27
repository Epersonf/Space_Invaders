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

    def spawn_new_wave(self, y_pos):
        for i in range(18):
            self.enemies.append(Enemy(self.gui, "Assets/ENEMY.PNG"))
            self.enemies[i].obj.x = i * self.enemies[i].obj.width
            self.enemies[i].obj.y = y_pos * self.enemies[i].obj.height

    def __init__(self, gui):
        self.gui = gui
        self.kbrd = gui.get_mouse()
        self.ms = gui.get_keyboard()
        self.char = Nave(gui, "Assets/NAVE.png")
        self.char.set_loc(gui.width // 2 - self.char.obj.width//2, gui.height - 100)
        self.stars = Stars(gui, 100)
        self.enemies.clear()
        self.spawn_new_wave(4)

    def draw(self, level, mode):
        self.gui.set_background_color((0, 0, 0))
        self.stars.draw()
        hit = False
        for i in self.enemies:
            if i.get_hit():
                hit = True
        for i in self.enemies:
            if hit:
                i.down()
            i.draw()
        self.char.draw(mode, self.enemies)

