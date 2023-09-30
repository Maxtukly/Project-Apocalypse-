import pygame
import tkinter
import sys
import ProcGen
pygame.mixer.init()

pygame.font.init()

black = (0, 0, 0)
p = pygame
tk = tkinter.Tk()
s = sys
x = tk.winfo_screenwidth()
y = tk.winfo_screenheight()

trigered = False
nowscene = 1
prewiousscene = None

screen = p.display.set_mode((x, y - 50))
ProcGen.screen = screen
pygame.display.set_caption('King of Apocalypse')

bg = pygame.image.load("sprites\Omega background fixed .png")
bg = pygame.transform.scale(bg, (tk.winfo_screenwidth(), tk.winfo_screenheight() - 50))
screen.blit(bg, (0, 0))

pygame.mixer.music.load("KoA menu theme vol.4")
p.mixer.music.play()

Allob = []

def changesound():
    if pygame.mixer.music.get_busy():
        p.mixer.music.stop()
    else:
        p.mixer.music.play()


class Button():
    def __init__(self, text, cordinates, mc, funtion, scene, texture):
        self.text = text
        self.scene = scene
        Allob.append(self)
        self.avaible = False
        self.funtion = funtion
        self.linkicon = None
        self.multiclicable = mc
        self.texture = texture
        self.w = self.texture.get_width()
        self.h = self.texture.get_height()
        self.cordinates = (cordinates[0] - self.w/2, cordinates[1] - self.h/2)
        font = pygame.font.Font('MiriamLibre-Regular.ttf', 32)
        text = font.render(self.text, True, black)
        textRect = text.get_rect()
        textRect.center = (self.texture.get_width() // 2, self.texture.get_height() // 2)
        self.texture.blit(text, textRect)

    def draw(self):
        screen.blit(self.texture, self.cordinates)
        self.avaible = True
        if self.linkicon != None:
            self.linkicon.draw()

    def is_ckiked(self):
        global trigered
        mousecords = p.mouse.get_pos()
        click = p.mouse.get_pressed()
        if self.cordinates[0] + self.w > mousecords[0] > self.cordinates[0] and self.cordinates[1] + self.h > mousecords[1] > self.cordinates[1]:
            if click[0] == 1 and self.avaible == True and trigered != True:
                trigered = True
                print("Pressed!")
                if self.funtion != None:
                    self.funtion()

                if self.multiclicable == True:
                    self.linkicon.chagestage()
            else:
                print("Not pressed")

class Menu_Button(Button):
    def __init__(self, text, cordinates, mc, funtion, scene, vector, texture):
        super().__init__(text, cordinates, mc, funtion, scene, texture)
        self.vector = vector
        if isinstance(self.scene, list):
            self.scenelist = self.scene
            self.scene = self.scenelist[0]


    def chage_menu(self):
        screen.blit(bg, (0, 0))
        global nowscene
        global prewiousscene
        prewiousscene = nowscene
        for i in Allob:
            if i.scene == self.scene + self.vector:
                i.draw()
            else:
                try:
                    if i != self:
                        if isinstance(i.scenelist, list):
                            if self.scene + self.vector in i.scenelist:
                                i.scene = self.scene + self.vector
                                i.draw()
                except:
                    i.avaible = False
        nowscene = self.scene + self.vector
        try:
            if isinstance(self.scenelist, list):
                if self.scene + self.vector in self.scenelist:
                    self.scene = self.scene + self.vector
                    self.draw()
        except:
            self.avaible = False

    def is_ckiked(self):
        global trigered
        mousecords = p.mouse.get_pos()
        click = p.mouse.get_pressed()
        if self.cordinates[0] + self.w > mousecords[0] > self.cordinates[0] and self.cordinates[1] + self.h > mousecords[
            1] > self.cordinates[1]:
            if click[0] == 1 and self.avaible == True and trigered != True:
                trigered = True
                print("Pressed!", self)
                self.chage_menu()
        else:
            if isinstance(self.scene, list):
                pass
            print("Not pressed")


class icon():
    def __init__(self, link, stageone, stagetwo):
        self.linkbutton = link
        self.linkbutton.linkicon = self
        self.scene = self.linkbutton.scene
        Allob.append(self)
        self.stage = 0
        self.stageone = stageone
        self.stagetwo = stagetwo
        self.cordinates = link.cordinates
        self.stageone = p.transform.scale(self.stageone, (self.linkbutton.w, self.linkbutton.h))
        if self.stagetwo != None:
            self.stagetwo = p.transform.scale(self.stagetwo, (self.linkbutton.w, self.linkbutton.h))
        self.currenttexture = self.stageone

    def draw(self):
        screen.blit(self.currenttexture, self.cordinates)

    def chagestage(self):
        if self.currenttexture == self.stageone and self.linkbutton.multiclicable == True:
            self.currenttexture = self.stagetwo
            self.linkbutton.draw()
            self.draw()
        else:
            self.currenttexture = self.stageone
            self.linkbutton.draw()
            self.draw()

startbutton = Menu_Button("start", (x/2, y/10), False, None, 1, 1, p.image.load("sprites\Button .png"))
createbutton = Menu_Button(ProcGen.Loadw.name, (x/2, y/10), False, None, 2, 1, p.image.load("sprites\Button .png"))
createbuttontwo = Menu_Button("New world", (x/2, y/10 * 2), False, None, 2, 1, p.image.load("sprites\Button .png"))
generation_button = Button("Go", (x/2, y/10 * 2), False, ProcGen.createworld, 3, p.image.load("sprites\Button .png"))
soundbutton = Button(None, (x - 300, y - 300), True, changesound, 0, pygame.transform.scale(p.image.load("sprites\small button .png"), (100, 100)))
soundicon = icon(soundbutton, p.image.load("sprites\soundon icon.png"), p.image.load("sprites\soundoff icon.png"))
Backbutton = Menu_Button(None, (x - (x - 50), y - (y - 50)), False, None, [2, 3, 4, 5, 6], -1, pygame.transform.scale(p.image.load("sprites\small button .png"), (100, 100)))
Backicon = icon(Backbutton, p.image.load("sprites\Go back.png"), None)
settingsbutton = Menu_Button("settings", (x/2, y/10 * 2), False, None, 1, -1, p.image.load("sprites\Button .png"))
Backbuttontwo = Menu_Button(None, (x - (x - 50), y - (y - 50)), False, None, [0, -1], 1, pygame.transform.scale(p.image.load("sprites\small button .png"), (100, 100)))
Backicontwo = icon(Backbuttontwo, p.image.load("sprites\Go back.png"), None)
quitbutton = Button("Exit", ((x/2), (y - 200)), False, p.quit, 1, p.image.load("sprites\Button .png"))

icon = pygame.image.load('sprites\KoA_icon.png')
pygame.display.set_icon(icon)

startbutton.draw()
settingsbutton.draw()
quitbutton.draw()

#'miriamlibre'
while True:
    for i in p.event.get():
        if i.type == p.QUIT:
            p.quit()
            sys.exit()
        if i.type == p.MOUSEBUTTONDOWN:
            for j in Allob:
                if isinstance(j, Button) or isinstance(j, Menu_Button):
                    j.is_ckiked()
            trigered = False

        if i.type == pygame.KEYDOWN:
            ProcGen.check(i)
            if i.key == p.K_n:
                pass

    pygame.display.flip()

