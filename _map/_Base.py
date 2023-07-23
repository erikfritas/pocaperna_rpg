import pygame as pyg
from pygame.locals import *
from _entities._Base import Base
from _configs import SURF_SIZE
from random import randint

class BaseMap:
    def __init__(self, surface, name, spritesheet):
        self.surface = surface
        self.name = name

        def spr_(img, size):
            return pyg.transform.scale(img, size)

        tree = pyg.image.load("res/recursos/madeiras/verao_arvore.png").convert_alpha()
        self.bs = 80
        self.sprites = [
             spr_(spritesheet.image_at([50*5,50,50,50]).convert(), (self.bs, self.bs)), # barreira
             spr_(spritesheet.image_at([0,0,50,50]).convert(), (self.bs, self.bs)), # grass block 1
             pyg.transform.scale2x(tree) #arvore
        ]

        self.blocks = [
            [self.sprites[0]],
            [self.sprites[1]],
            [self.sprites[1], self.sprites[2]], # arvore
            [self.sprites[0]],
            [],
        ]

        wh = [40, 70]
        self.Player = Base(surface, [wh[0], wh[1], (SURF_SIZE[0]/2)-wh[0]/2, (SURF_SIZE[1]/2)-wh[1]/2], 10)
        self.pos = self.Player.pos

        self.itens = [
            "barreira", "espaco", "arvore", "agua", "area", "caverna", "void", "workbench"
        ]

        self.map = []

        self.generate()

    def generate(self):
        with open("_map/map.dat", "r") as _map:
            for l in _map.readlines():
                self.map.append(l.replace("\n", ""))

    def update(self, clock, nav):
        self.Player.update(clock, nav)
        self.pos = self.Player.pos

    def render(self):
        l = self.bs
        iy = 0
        ix = 0
        for y in self.map:
            ix = 0
            for x in self.map[iy]:
                for b in self.blocks[int(x)]:
                    self.surface.blit(b, (ix*l-self.pos[0], iy*l-self.pos[1]))
                ix += 1
            iy += 1

        self.Player.render()
            

