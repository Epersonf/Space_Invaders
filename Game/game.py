from Game.PPlay.window import *
from Game.menu import *
from Game.game_itself import *
from Game.mode import *
from Game.Name_Gui import *
from Game.Rank_Menu import *

gui = Window(1024, 768)
gui.set_title("Invaders")


def get_scores():
    array = []
    try:
        file = open("rank.txt", "r")
        st = file.read().split("\n")
        for i in range(len(st)):
            array.append([])
            array[i] = st[i].split("-")
        file.close()
        return array
    except:
        file = open("rank.txt", "w")
        file.write("JOSEPH-100\n")
        file.write("EPERSON-90\n")
        file.write("BIGO-80\n")
        file.write("ALFRED-70\n")
        file.write("ULTRAMAN-60\n")
        file.write("JAYJAY-50\n")
        file.write("ADAM-40\n")
        file.write("KEVIN-30\n")
        file.write("KURT-20\n")
        file.write("KENNAN-10\n")
        file.close()
        return get_scores()
    return


all_scores = get_scores()


def store_scores():
    file = open("rank.txt", "w")
    for i in range(10):
        file.write(all_scores[i][0] + "-" + all_scores[i][1] + "\n")
    file.close()

#0 = menu, 1 = mode select, 2 = ranking, 3 = game itself
level = [-1]

debug = True
fps = 0
sss = 0
contador = 0
score = [0]
lives = [3]
record = 20


#levels
mm = Main_Menu(gui)
gm = Game_Itself(gui, score)
mg = Mode_Gui(gui)
ni = Name_Gui(gui)
rm = Rank_Menu(all_scores, gui)

#easy = 1, medium = 2, hard = 3
mode = [1]

name = [""]

kbrd = gui.get_keyboard()
ms = gui.get_mouse()

while True:
    prev_lvl = level.copy()
    if level[0] == -1:
        ni.draw(level, name)
    elif level[0] == 0:
        mm.draw(level, mode)
    elif level[0] == 3:
        gm.draw(level, mode, lives)
        gui.draw_text("Name: " + name[0], 0, 0, 32, (255, 255, 255))
        gui.draw_text("Score: " + str(score[0]), 0, 32, 32, (255, 255, 255))
        gui.draw_text("Lives: " + str(lives[0]), 0, 64, 32, (255, 255, 255))
        if lives[0] <= 0:
            if name[0] == "":
                name[0] = "GUEST"
            if len(all_scores) == 0:
                all_scores.append([name[0], str(score[0])])
            for i in range(len(all_scores)-1):
                if score[0] > int(all_scores[i][1]):
                    all_scores.insert(i, [name[0], str(score[0])])
                    all_scores.pop(len(all_scores) - 1)
                    break
            all_scores = all_scores[0:10]
            store_scores()
            level[0] = 0
    elif level[0] == 1:
        mg.draw(level, mode)
    elif level[0] == 2:
        rm.draw()

    if prev_lvl != level:
        score[0] = 0
        lives[0] = 3
        gm.char.fire.clear()
        gm = Game_Itself(gui, score)

    contador += gui.delta_time()
    sss += 1
    if contador >= 1:
        contador = 0
        fps = sss
        sss = 0
    gui.draw_text(str(fps), 0, gui.height - 12, 12, (255, 255, 255))

    if kbrd.key_pressed("ESC"):
        level[0] = 0
    gui.update()
