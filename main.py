import pygame as pg

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pg.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pg.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

running = True

while running:
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    screen.fill((255,255,255))

    surf = pg.Surface((50,50))

    surf.fill((0,0,0))
    rect = surf.get_rect()

    screen.blit(surf, (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    pg.display.flip()