class Rank_Menu:

    ac = None
    gui = None
    def __init__(self, all_scores, gui):
        self.gui = gui
        self.ac = all_scores

    def draw(self):
        self.gui.set_background_color((0, 0, 0))
        self.loc = 0
        build = "Best players:"
        for i in self.ac:
            self.print_build(build)
            build = i[0] + " ... " + i[1]
        self.print_build(build)

    size = 40
    loc = 0
    def print_build(self, build):
        self.loc += self.size
        self.gui.draw_text(build, 0, self.loc, self.size, (255, 255, 255))

