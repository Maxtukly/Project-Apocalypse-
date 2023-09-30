import pygame
import tkinter
import random
import pickle
import copy
import math
'''B - create world
S - save world
L - load world 
C - clean map'''


pygame.init()
p = pygame
m = math
tk = tkinter.Tk()

x = 500
y = 500
screen = None
color_e = (0, 100, 0)
color_ws = (0, 75, 100)
color_w = (0, 0, 100)
rmcords = [0, 0]
zk = []  # зайняті позиціїї
listforocean = []

# Just buffer for comfort


class Buffer:
    def __init__(self):
        self.worldsize = 0
        self.map = []
        self.file = None
        self.name = ""


Loadw = Buffer()


class UCube:
    def __init__(self, co, color, gtype, world):
        self.color = color
        self.cords = co
        self.size = world.worldsize
        self.suportcords = copy.deepcopy(self.cords)
        self.stopcords = [self.suportcords[0] + world.worldsize, self.suportcords[1] + world.worldsize]
        self.surfacex = range(self.suportcords[0], self.stopcords[0])
        self.surfacey = range(self.suportcords[1], self.stopcords[1])
        self.type = gtype

    def draw(self):
        r = p.Rect(self.cords[0], self.cords[1], self.size, self.size)
        p.draw.rect(screen, self.color, r, 0)


class Island:
    def __init__(self, size, world):

        # all needed variables for island generation

        self.size = size
        self.world  = world

    def birth(self):
        n = True
        global x
        global y
        xx = copy.deepcopy(x)
        yy = copy.deepcopy(y)
        seq = [self.world.worldsize, -self.world.worldsize, 0]
        seq10 = [self.world.worldsize, -self.world.worldsize]
        px = random.randrange(60, xx, self.world.worldsize)
        py = random.randrange(60, yy, self.world.worldsize)
        zkl = []

        # Main loop\core of island building

        while n is True:
            xc = px + random.choice(seq)
            if xc > xx:
                return
            yc = py + random.choice(seq)
            if yc > yy:
                return
            if xc == px and yc == py:
                rn = random.randint(0, 1)
                if rn == 0:
                    xc = xc + random.choice(seq10)
                if rn == 1:
                    yc = yc + random.choice(seq10)

            prcord = [xc, yc]
            px = xc
            py = yc
            if prcord in listforocean:
                print("Ops")
            else:
                smthng = UCube(prcord, color_e, "Earth", Loadw)
                listforocean.append(prcord)
                zk.append(smthng)
                zkl.append(smthng)
            if len(zkl) >= self.size:
                n = False

        # Filling gaps and creating shore

    def fill(self):
        zkxp = []
        for u in zk:
            cc = u.cords
            zkxp.append(cc)
        zkx = copy.deepcopy(zk)
        zx = copy.deepcopy(zk)
        zky = copy.deepcopy(zk)
        zy = copy.deepcopy(zk)
        for g in zkx:
            g.cords[0] += self.world.worldsize
            if g.cords not in zkxp:
                print("nope", g.cords)
                smtn = UCube(g.cords, color_ws, "Shore", self.world)
                zk.append(smtn)
                listforocean.append(g.cords)
        for g in zx:
            g.cords[0] -= self.world.worldsize
            if g.cords not in zkxp:
                print("nope", g.cords)
                smtn = UCube(g.cords, color_ws, "Shore", self.world)
                zk.append(smtn)
                listforocean.append(g.cords)
        for g in zky:
            g.cords[1] += self.world.worldsize
            if g.cords not in zkxp:
                print("nope", g.cords)
                smtn = UCube(g.cords, color_ws, "Shore", self.world)
                zk.append(smtn)
                listforocean.append(g.cords)
        for g in zy:
            g.cords[1] -= self.world.worldsize
            if g.cords not in zkxp:
                print("nope", g.cords)
                smtn = UCube(g.cords, color_ws, "Shore", self.world)
                zk.append(smtn)
                listforocean.append(g.cords)

    def spawn(self):
        self.birth()
        self.fill()



class World:
    def __init__(self):

        # Really valuable stuff\needed variables for code to work

        self.num = 5
        inpworsize = (input("World size: "))  # Inputting world size
        self.worldsize = 15

        # Declairing size of world

        if inpworsize == "Tiny":
            self.worldsize = 20
        elif inpworsize == "Small":
            self.worldsize = 15
        elif inpworsize == "Medium":
            self.worldsize = 10
        elif inpworsize == "Big":
            self.worldsize = 5

        """actually size of squares, smaller squares = more spase for another squares, so world
        is bigger"""

        # Main data of world in global perspective, I mean name of file and actual world

        self.name = str(input("Worlds name: "))
        self.file = "World-" + str(self.name) + ".obj"
        self.loaded = False
        self.map = None

    def spawn_ocean(self):

        # Spawning of ocean

        xo = 0
        yo = 0
        while True:
            if yo >= y:
                break
            ok = [xo, yo]
            if ok not in listforocean:
                smo = UCube(ok, color_w, "Ocean", self)
                zk.append(smo)
                print(ok)
                print("spawn ocean", ok)
            else:
                print("Land", ok)
            if xo >= x - self.worldsize:
                yo += self.worldsize
                xo = 0
            else:
                xo += self.worldsize

    def creating(self):

        # Initiation of creating

        for rp in range(0, self.num):
            y = Island(30, Loadw)
            y.spawn()
        self.spawn_ocean()
        self.map = zk
        for h in Loadw.map:
            h.draw()


def save():
    # saving
    k = Loadw
    saving = open(k.file, "wb")
    pickle.dump(Loadw, saving)
    saving.close()


def upload(mmap):
    # loading map from save
    for i in mmap:
        i.draw()


def clean(llist):
    for ir in llist:
        ir.draw()
        del ir
    screen.fill((0, 0, 0))
    print(zk)
    print("Deleting complete")


def load():
    # loading save
    global Loadw
    nome = input("Name of world:")
    sav = open("World-" + nome + ".obj", "rb")
    s = pickle.load(sav)
    Loadw = s
    upload(s.map)
    sav.close()


"""def bug_destroyer():
    for h in Loadw.map:
        if h.type == "Bug":
            Loadw.map.remove(h)"""


def createworld():
    # making world
    global Loadw
    Loadw = World()
    Loadw.creating()


def check(i):
    # global rmcords
    """if i.type == p.MOUSEBUTTONDOWN:
        mousecords = p.mouse.get_pos()
        click = p.mouse.get_pressed()
        for i in Loadw.map:
            if i.cords[0] + worldsize > mousecords[0] > i.cords[0] and i.cords[1] + worldsize > mousecords[1] > /
            i.cords[1]:
                if click[0] == 1:
                    print(i.type)
                    i.color = (60, 30, 10)
                    if i.type == "Earth":
                        i.color = (100, 63, 90)
                    i.draw()
                else:
                    rmcords = [m.floor(mousecords[0] / 10) * 10, m.floor(mousecords[1] / 10) * 10]
                    print(rmcords)
                    fix()"""

    if i.type == pygame.KEYDOWN:
        if i.key == p.K_b:
            createworld()
        if i.key == p.K_s:
            save()
        if i.key == p.K_l:
            load()
        if i.key == p.K_c:
            clean(zk)

