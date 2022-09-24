import pygame
from pygame.locals import *
import time
import random
 
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)

pygame.init()
screen = pygame.display.set_mode((1000, 640))
clock = pygame.time.Clock()





font2 = pygame.font.Font('./font/Grand9K Pixel.ttf', 62)
text = 'Hello Max, the best DM.'
text_2 = 'Thanls for creating this team.'
text_3 = 'We will have the best results!'
letter = 0
letter_2 = 0
letter_3 = 0
textuse = ''
textuse_2 = ''
textuse_3 = ''


running = True
background = BLACK
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill(background)
    if letter < len(text)-1:
        img1 = font2.render(textuse +text[letter], True, (255,255,255))
        screen.blit(img1, (10, 10))
        textuse += text[letter]
        letter += 1

    elif letter_2 < len(text_2)-1:
        img2 = font2.render(textuse_2 +text_2[letter_2], True, (255,255,255))
        screen.blit(img2, (10, 110))
        screen.blit(img1, (10, 10))
        textuse_2 += text_2[letter_2]
        letter_2 += 1
    elif letter_3 < len(text_3)-1:
        img3 = font2.render(textuse_3 +text_3[letter_3], True, (255,255,255))
        screen.blit(img3, (10, 210))
        screen.blit(img2, (10, 110))
        screen.blit(img1, (10, 10))
        textuse_3 += text_3[letter_3]
        letter_3 += 1

    pygame.display.update()
    clock.tick(random.randint(5, 15))

pygame.quit()