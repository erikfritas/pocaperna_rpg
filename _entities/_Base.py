import pygame as pyg
from pygame.locals import *
from _configs import FPS, MOVEEVENT


class Base:
    def __init__(self, surface, rect, speed):
        self.surface = surface
        self.rect = rect # w h x y
        self.speed = speed

        self.pos = [400, 800] # x y
        self.map_limit = [800, 1600]

        self.kpress = [False, False, False, False] # w a s d
        self.pside = True

        self.upd = self.updp

        self.sprite = []
        self.spr_time = 0
        self.update_spr()

    def updp(self):
        pass

    def update_spr(self):
        imgl = pyg.image.load(
            f"res/player/{'walk' if True in self.kpress else 'idle'}/left_{self.spr_time}.png")
        imgr = pyg.image.load(
            f"res/player/{'walk' if True in self.kpress else 'idle'}/right_{self.spr_time}.png")
        self.sprite = [
            pyg.transform.scale(imgl, (self.rect[0], self.rect[1])), # left
            pyg.transform.scale(imgr, (self.rect[0], self.rect[1])), # right
        ]

    def walk(self):
        if True in self.kpress:
            if self.kpress[0]:
                self.pos[1] -= self.speed
            if self.kpress[2]:
                self.pos[1] += self.speed

            if self.kpress[1]:
                self.pos[0] -= self.speed
            if self.kpress[3]:
                self.pos[0] += self.speed
        self.upd = self.update_spr

    def control(self, e):
        if e.type == KEYDOWN:
            if e.key == K_w:
                self.kpress[0] = True
            if e.key == K_s:
                self.kpress[2] = True

            if e.key == K_a:
                self.kpress[1] = True
                self.pside = True
            if e.key == K_d:
                self.kpress[3] = True
                self.pside = False

        if e.type == KEYUP:
            if e.key == K_w:
                self.kpress[0] = False
            if e.key == K_s:
                self.kpress[2] = False

            if e.key == K_a:
                self.kpress[1] = False
            if e.key == K_d:
                self.kpress[3] = False


    def render_spr(self):
        return self.sprite[0] if self.pside else self.sprite[1]

    def update(self, clock, nav):
        clock.tick(FPS)
        for e in pyg.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                pyg.quit()
                exit()

            if e.type == MOVEEVENT:
                self.spr_time = 1 if self.spr_time == 0 else 0
            
            self.control(e)

        self.walk()
        self.upd()

    def render(self):
        self.surface.blit(self.render_spr(), [self.rect[2], self.rect[3]])

