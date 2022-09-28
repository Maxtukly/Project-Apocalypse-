import pygame as pg
import ptext


pg.init()
screen = pg.display.set_mode((640, 480))
clock = pg.time.Clock()
BG_COLOR = pg.Color('gray12')
BLUE = pg.Color('dodgerblue')
# Triple quoted strings contain newline characters.
text_orig = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua.

Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum."""

# Create an iterator so that we can get one character after the other.
text_iterator = iter(text_orig)
text = ''

done = False
while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        # Press 'r' to reset the text.
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_r:
                text_iterator = iter(text_orig)
                text = ''

    if len(text) < len(text_orig):
        # Call `next(text_iterator)` to get the next character,
        # then concatenate it with the text.
        text += next(text_iterator)

    screen.fill(BG_COLOR)
    pg.draw(text, (10, 10), color=BLUE)  # Recognizes newline characters.
    pg.display.flip()
    clock.tick(60)

pg.quit()