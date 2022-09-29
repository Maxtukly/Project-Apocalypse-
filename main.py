import pygame as p
import pyautogui

from background import BackGround
from character import Character
from menu import Menu




p.init()
width, height = pyautogui.size()
screen = p.display.set_mode([width, height])
clock = p.time.Clock()
background = BackGround(p, 'hello from bg')
character = Character(p, 'hello from chaacter')
menu = Menu(p, screen)

FPS = 30






screen.fill((0, 0, 0))
change = 0

running = True
while running:

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False




    p.display.update()
    clock.tick(FPS)
p.quit()

