from Game.ship import *
from Game.enemy import *
from Game.stars_ambient import *
from Game.ovni import *
from Game.s_fire import *
class Game_Itself:

    gui = None
    kbrd = None
    ms = None
    char = None
    stars = None
    high = 0
    enemies = []
    score = []
    ufos = []
    sfire = None

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
        self.sfire = S_fire(gui)
        self.high = 0
        self.enemies.clear()
        self.ufos.clear()
        self.gui = gui
        self.ms = gui.get_mouse()
        self.kbrd = gui.get_keyboard()
        self.char = Nave(gui, "Assets/NAVE.png", self.score)
        self.char.set_loc(gui.width // 2 - self.char.obj.width // 2, gui.height - 100)
        self.stars = Stars(gui, 100)
        self.enemies.clear()
        self.enemyAmt = 4
        for i in range(3):
            self.high = self.spawn_new_wave(i)

    def __init__(self, gui, score):
        self.score = score
        self.reset(gui)

    count = 0
    count_ufo = 30
    count_sf = 30
    enemyAmt = 4
    
    def draw(self, level, mode, lives):
        self.gui.set_background_color((0, 0, 0))
        self.stars.draw()
        if len(self.enemies) == 0:
            self.enemyAmt += 1
            for i in range(self.enemyAmt):
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
        self.count_ufo += self.gui.delta_time()
        self.count_sf += self.gui.delta_time()

        dec = 0
        decUf = 0
        for i in range(len(self.ufos)):
            self.ufos[i-decUf].draw()
            if self.ufos[i-decUf].obj.x > self.gui.width:
                self.ufos.pop(i-decUf)
                decUf += 1
            for j in range(len(self.char.fire)):
                if self.char.fire[j-dec].collided(self.ufos[i-decUf].obj):
                    self.ufos.pop(i-decUf)
                    self.char.fire.pop(j-dec)
                    self.count_ufo = randint(0, 8)
                    self.score[0] += 10
                    dec += 1
                    break
            decUf += 1

        store = self.sfire.draw()
        if store:
            brk = len(self.enemies)
            i = 0
            while i < brk:
                if self.sfire.obj.collided(self.enemies[i].obj):
                    self.enemies.pop(i)
                    i -= 1
                    brk -= 1
                i += 1
        if self.kbrd.key_pressed("SPACE") and self.count_sf >= 5 and not store:
            self.sfire.obj.x = self.char.obj.x + self.char.obj.width/2
            self.sfire.obj.y = self.char.obj.y
            self.count_sf = 0

        if self.count_ufo >= 10 and len(self.ufos) <= 1:
            self.count_ufo = 0
            self.ufos.append(Ovni("Assets/OVNI.PNG", self.gui))
            self.ufos[len(self.ufos)-1].set_location(0, randint(0, self.gui.height/3))

        if self.count >= 1:
            self.count = 0
            self.enemies_fire()

