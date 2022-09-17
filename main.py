from turtle import width
import pygame as p
import pyautogui

width, height = pyautogui.size()

from background import BackGround


from character import Character


p.init()
screen = p.display.set_mode([width, height])

background = BackGround(p, 'hello from bg')
character = Character(p, 'hello from chaacter')

screen.fill((0, 0, 0))
change = 0

running = True
while running:

    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    if change == 0:
        screen.fill((255,255,255))
        change = 1
    else: 
        screen.fill((0,0,0))
        change = 0


    p.display.flip()

p.quit()

