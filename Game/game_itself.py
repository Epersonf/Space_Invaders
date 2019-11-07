from Game.ship import *
from Game.enemy import *
from Game.stars_ambient import *

class Game_Itself:

    gui = None
    kbrd = None
    ms = None
    char = None
    stars = None
    high = 0
    enemies = []
    score = []

    def enemies_fire(self):
        self.enemies[randint(0, len(self.enemies) - 1)].fire_enemy()

    def spawn_new_wave(self, y_pos):
        tamanho = len(self.enemies) - 1
        for i in range(12):
            self.enemies.append(Enemy(self.gui, "Assets/ENEMY.PNG"))
            self.enemies[i + tamanho].obj.x = i * self.enemies[i].obj.width
            self.enemies[i + tamanho].obj.y = y_pos * self.enemies[i].obj.height
        return y_pos * self.enemies[i].obj.height + self.enemies[i].obj.height

    def reset(self, gui):
        self.high = 0
        self.enemies.clear()
        self.gui = gui
        self.kbrd = gui.get_mouse()
        self.ms = gui.get_keyboard()
        self.char = Nave(gui, "Assets/NAVE.png", self.score)
        self.char.set_loc(gui.width // 2 - self.char.obj.width // 2, gui.height - 100)
        self.stars = Stars(gui, 100)
        self.enemies.clear()
        for i in range(3):
            self.high = self.spawn_new_wave(i)

    def __init__(self, gui, score):
        self.score = score
        self.reset(gui)

    count = 0
    def draw(self, level, mode, lives):
        self.gui.set_background_color((0, 0, 0))
        self.stars.draw()
        if len(self.enemies) == 0:
            for i in range(8):
                self.high = self.spawn_new_wave(i)
        hit = False
        for i in self.enemies:
            if i.get_hit():
                hit = True
        for i in self.enemies:
            if i.obj.y > self.gui.height - self.char.obj.height:
                lives[0] = 0
            if hit:
                self.high += self.enemies[0].obj.height
                record = 0
                for k in range(len(self.enemies)):
                    if self.enemies[k].obj.y > record:
                        record = self.enemies[k].obj.y
                self.high = record + self.enemies[k].obj.height
                i.down()
            i.draw(self.char, lives, mode)
        self.char.draw(mode, self.enemies, self.high)
        self.count += self.gui.delta_time()
        if self.count >= 1:
            self.count = 0
            self.enemies_fire()

