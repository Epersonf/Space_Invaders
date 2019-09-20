from Game.PPlay.sprite import *

class Nave:


    vel = 2

    fire = []
    count = 0
    gui = None
    obj = None
    keyboard = None

    def __init__(self, g, path, x=0, y=0):
        self.gui = g
        self.obj = Sprite(path)
        self.keyboard = self.gui.get_keyboard()
        self.obj.set_position(x, y)

    def set_loc(self, x, y):
        self.obj.set_position(x, y)

    def draw(self, mode):
        if self.keyboard.key_pressed("LEFT") and self.obj.x > 0:
            self.obj.move_x(-self.vel * 1/(mode[0]*0.8))
        elif self.keyboard.key_pressed("RIGHT") and self.obj.x < self.gui.width - self.obj.width:
            self.obj.move_x(self.vel * 1/(mode[0]*0.8))
        if self.count < 60:
            self.count += 200 * self.gui.delta_time() * 1/(mode[0]*0.8)
        else:
            self.count = 60
        if self.keyboard.key_pressed("UP") and self.count == 60:
            self.count = 0
            self.fire.append(Sprite("Assets/FIRE.png"))
            x, y = self.obj.x, self.obj.y
            sub = self.obj.width//2 - self.fire[len(self.fire)-1].width//2
            self.fire[len(self.fire)-1].set_position(x + sub, y + self.obj.height//2)


        dec = 0
        for i in range(len(self.fire)):
            if self.fire[i-dec].y < -self.fire[i-dec].height:
                self.fire.pop(i-dec)
                dec += 1
                continue
            self.fire[i-dec].move_y(-3)
            self.fire[i-dec].draw()


        self.obj.draw()
