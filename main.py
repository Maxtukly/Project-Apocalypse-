import pygame as p
import pyautogui
import os

from background import BackGround
from character import Character
from menu import Menu
from upload import Upload



p.init()
width, height = pyautogui.size()
screen = p.display.set_mode([width, height])
clock = p.time.Clock()
background = BackGround(p, 'hello from bg')
character = Character(p, 'hello from chaacter')
menu = Menu(p, screen)

FPS = 30

######Loading######
upld = Upload(p, os)
ground_textures = upld.upload_textures(filepath="./sprites/textures/ground_textures/")




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