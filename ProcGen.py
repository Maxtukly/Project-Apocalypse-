import pygame
import tkinter
import random
import pickle
import copy
import sys
'''B - створити світ, в консолі треба ввести розміри трьох островів
S - зберігає карту
L - загружає карту(well yes, but actualy yes)
C - очищує карту
Q - вихід'''

pygame.init()
p = pygame
tk = tkinter.Tk()
s = sys


num = int(input("Number of islands: "))
inpworsize = int(input("World size: ")) #Розмір світу який вводить гравець, максимум 20
worldsize = 21 - inpworsize
"""розмір клітинок, чим більше вводять - тим менше клітинки, 
чим менше клітинки - тим більше влізе, а значить світ більше"""


if worldsize <= 0:
    print("To big, setting max world size...")
    worldsize = 1

x = tk.winfo_screenwidth()
y = tk.winfo_screenheight()
screen = p.display.set_mode((x, y))
color_e = (0, 100, 0)
color_ws = (0, 75, 100)
color_w = (0, 0, 100)
zk = [] # зайняті позиціїї

class UCube:
    def __init__(self, co, color, type):
            self.color = color
            self.cords = co
            self.type = type

    def draw(self):
        r = p.Rect(self.cords[0], self.cords[1], worldsize, worldsize)
        p.draw.rect(screen, self.color, r, 0)

class World():
    def __init__(self):
        self.name = input("Name of world:")
        self.size = None
        self.file = "World-" + self.name + ".obj"
        self.loaded = False
        self.map = None

Loadw = World()
Loadw.size = worldsize

def spawn_island(size, xx, yy):
    # створення світу
    n = True
    # color_w = (random.randint(0, 100), random.randint(0, 100), random.randint(0, 100))
    seq = [worldsize, -worldsize, 0]
    seq10 = [worldsize, -worldsize]
    px = random.randrange(60, xx, worldsize)
    py = random.randrange(60, yy, worldsize)
    zkl = []
    while px in zk:
        px = random.randint(20, 1180)
    while py in zk:
        py = random.randint(20, 780)
    while n is True:
        x = px + random.choice(seq)
        if x > xx:
            return
        y = py + random.choice(seq)
        if y > yy:
            return

        prcord = [x, y]
        px = x
        py = y
        if prcord in zk and prcord in zkl:
            pass
        else:
            smthng = UCube(prcord, color_e, "Earth")
            zk.append(smthng)
            zkl.append(smthng)
        if len(zkl) >= size:
            n = False


def fill():
    # заповнення непотрібних участків
    zkxp = []
    for u in zk:
        cc = u.cords
        zkxp.append(cc)
    zkx = copy.deepcopy(zk)
    zky = copy.deepcopy(zk)
    tim = 0
    for g in zkx:
        g.cords[0] += worldsize
        if g.cords not in zkxp:
            tim += 1
            print("nope", tim, g.cords)
            smtn = UCube(g.cords, color_ws, "Shore")
            zk.append(smtn)

Loadw.map = zk

def spawn_ocean():
    ok = [0, 0]
    ozk = []
    for j in zk:
        ozk.append(j.cords)
    while True:
        if ok[1] > y:
            break
        if ok not in ozk:
            smo = UCube(ok, color_w, "Ocean")
            zk.append(smo)
            print("spawn ocean", ok)
        else:
            print("Land", ok)
        if ok[0] >= x:
            ok[1] += worldsize
            ok[0] = 0
        else:
            ok[0] += worldsize


def save():
    # збереження карти
    k = Loadw
    saving = open(k.file, "wb")
    pickle.dump(Loadw, saving)
    saving.close()


def upload(map):
    # завантаження карти з зберігання
    for i in map:
        i.draw()

def clean(list):
    for i in list:
        del i
    screen.fill((0, 0, 0))
    print("Deleting complete")

def load():
    # завантаження збереження
    nome = input("Name of world:")
    sav = open("World-" + nome + ".obj", "rb")
    s = pickle.load(sav)
    upload(s.map)
    sav.close()

while True:
    for i in p.event.get():
        if i.type == p.QUIT:
            p.quit()
            sys.exit()
        if i.type == pygame.KEYDOWN:
            if i.key == p.K_b:
                # побудова світу
                for a in range(0, num):
                    spawn_island(50, x, y)
                fill()
                spawn_ocean()
                for j in Loadw.map:
                    j.draw()
                print(zk)
            if i.key == p.K_s:
                save()
            if i.key == p.K_l:
                load()
            if i.key == p.K_c:
                clean(zk)
            if i.key == p.K_q:
                p.quit()
                sys.exit()
    pygame.display.update()


