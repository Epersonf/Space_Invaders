from Game.PPlay.sprite import *

class name_input:

    letters = ["A",  "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    letter = "_"
    x = 0
    y = 0
    size = None
    up = None
    down = None
    gui = None
    mouse = None

    def __init__(self, gui,  x_set, y_set, default, size):
        self.gui = gui
        self.mouse = gui.get_mouse()
        self.up = Sprite("Assets/Arrow_Up.png")
        self.down = Sprite("Assets/Arrow_Down.png")
        self.x = x_set
        self.y = y_set
        self.up.x = x_set
        self.down.x = x_set
        self.up.y = y_set - size
        self.down.y = y_set + size
        self.letter = default
        self.size = size

    def get_index(self, a):
        if a == "_":
            return 0
        for i in range(len(self.letters)):
            if self.letters[i] == a:
                return i

    def move(self, cmd="down"):
        first = 0
        second = self.letters[len(self.letters) - 1]
        sum = -1
        if cmd == "up":
            first = len(self.letters) - 1
            second = self.letters[0]
            sum = 1
        if self.get_index(self.letter) == first:
            self.letter = second
        else:
            self.letter = self.letters[self.get_index(self.letter) + sum]

    def mouse_click(self, spr):
        if spr.x <= self.mouse.get_position()[0] <= spr.x + spr.width:
            if spr.y <= self.mouse.get_position()[1] <= spr.y + spr.height and self.mouse.is_button_pressed(1):
                return True
        return False

    def set_location(self, x, y):
        self.up.y = y - self.size - self.up.height
        self.down.y = y + self.size

        self.up.x = x
        self.down.x = x

    count = 0
    def draw(self):
        self.count += self.gui.delta_time()
        if self.count >= 0.2:
            self.count = 1
            if self.mouse_click(self.up):
                self.move("up")
                self.count = 0
            elif (self.mouse_click(self.down)):
                self.move()
                self.count = 0
        self.up.draw()
        self.down.draw()
        self.gui.draw_text(self.letter, self.x-5, self.y-10, self.size, (255, 255, 255))
