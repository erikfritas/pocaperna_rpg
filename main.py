import pygame as pyg
from pygame.locals import *
from _configs import *
from _map._Base import BaseMap
from _menu import Menu
from spritesheet.Sprites import SpriteSheet

clock = pyg.time.Clock()

class Game:
    def __init__(self):
        self.done = False
        self.Menu = Menu(display)
        self.Map = BaseMap(display, "overworld", SpriteSheet("res/spritesheet/spritesheet.png"))

        self.pages = [
            [self.Menu.update, self.Menu.render],
            [self.Map.update, self.Map.render]
        ]
        self.pIndex = 0

    def navigate(self, index):
        self.pIndex = index

    def loop(self):
        while not self.done:
            self.pages[self.pIndex][0](clock, self.navigate)

            display.fill((0, 0, 10))
            self.pages[self.pIndex][1]()

            pyg.display.update()

if __name__ == "__main__":
    game = Game()
    game.loop()
