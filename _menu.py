import pygame as pyg
from pygame.locals import *
from _configs import FPS

pyg.init()

font_name = "carlito"
font_title = pyg.font.SysFont(font_name, 150)
font_opt = pyg.font.SysFont(font_name, 50)

class Menu:
    def __init__(self, surface):
        self.surface = surface
        self.name = font_title.render("Retro's Craft", True, (250, 250, 255))
        self.spc_p = False

    def controls(self, e, nav):
        if e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                self.spc_p = True

        if e.type == MOUSEBUTTONUP:
            if e.button == 1:
                nav(1)

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                self.spc_p = True

        if e.type == KEYUP:
            if e.key == K_SPACE:
                nav(1)

    def update(self, clock, nav):
        clock.tick(FPS)
        for e in pyg.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == K_ESCAPE:
                pyg.quit()
                exit()

            self.controls(e, nav)

    def render(self):
        self.surface.fill((0, 0, 10))
        self.surface.blit(self.name, (335, 200))
        self.surface.blit(font_opt.render("press space to new game", True, (200, 200, 255)), (420, 600))
