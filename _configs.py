import pygame as pyg
from pygame.locals import *
import os

FPS = 120

os.environ['SDL_VIDEO_CENTERED'] = '1'

pyg.init()
info = pyg.display.Info()

screen_width, screen_height = info.current_w, info.current_h
window_width, window_height = screen_width-10, screen_height-50
WINDOW_SIZE = [(window_width+4)*2, (window_height+50)*2]
SURF_SIZE = [window_width+4, window_height+50]

display = pyg.display.set_mode(WINDOW_SIZE, FULLSCREEN)  # FULLSCREEN padrao, RESIZABLE dev_mode
screen = pyg.Surface(SURF_SIZE)
pyg.display.update()

MOVEEVENT, t = pyg.USEREVENT+1, 250
pyg.time.set_timer(MOVEEVENT, t)

