from Game.PPlay.sprite import *

class Enemy:

    fire_enemy_array = None
    obj = None
    gui = None
    x_vel = 50
    y_vel = None
    hit = False
    dist = 0

    def __init__(self, gui, path):
        self.obj = Sprite(path)
        self.gui = gui
        self.y_vel = self.obj.height
        self.fire_enemy_array = []

    def get_hit(self):
        if self.hit:
            self.hit = False
            return not self.hit
        else:
            return self.hit

    def fire_enemy(self):
        self.fire_enemy_array.append(Sprite("Assets/FIRE.png"))
        self.fire_enemy_array[len(self.fire_enemy_array) - 1].x = self.obj.x + self.obj.width / 2
        self.fire_enemy_array[len(self.fire_enemy_array) - 1].y = self.obj.y + self.obj.height / 2

    def down(self):
        self.obj.y += self.y_vel
        self.x_vel = -self.x_vel
        self.obj.x += self.x_vel * self.gui.delta_time() * 5


    def draw(self, char, lives, mode):
        dec = 0
        for i in range(len(self.fire_enemy_array)):
            self.fire_enemy_array[i - dec].y += self.gui.delta_time() * 500 * mode[0]
            if char.obj.collided(self.fire_enemy_array[i - dec]):
                lives[0] -= 1
                self.fire_enemy_array.pop(i - dec)
                dec += 1
                continue
            if self.fire_enemy_array[i - dec].y > self.gui.height:
                self.fire_enemy_array.pop(i - dec)
                dec += 1
                continue
            self.fire_enemy_array[i - dec].draw()

        self.obj.x += self.x_vel * self.gui.delta_time()

        if self.obj.x < 0 or self.obj.x > self.gui.width - self.obj.width:
            self.hit = True

        self.obj.draw()
