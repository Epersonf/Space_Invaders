from Game.game import *

Play = Btn("Game/Assets/BTN.png", "Play", gui, gui.width / 2, gui.height / 2)
Mode = Btn("Game/Assets/BTN.png", "Mode", gui, gui.width / 2)
Ranking = Btn("Game/Assets/BTN.png", "Rank", gui, gui.width / 2)
Exit = Btn("Game/Assets/BTN.png", "Exit", gui, gui.width / 2)


def draw_m():
    Play.draw()
    Mode.draw()
    Ranking.draw()
    Exit.draw()
