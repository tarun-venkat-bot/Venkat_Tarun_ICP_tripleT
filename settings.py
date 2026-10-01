#screen dimensions
import pygame as pg

WIDTH = 1024
HEIGHT = 768
TILESIZE = 32
FPS = 30

#colors
WHITE = (255,255,255)
BLUE = (50, 50, 255)
GREEN = (0, 255, 0)
BLACK = (0,0,0)
RED = (255, 0,0)
PURE_BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
MAROON = (128, 0, 0)
FOREST_GREEN = (0, 128, 0)
NAVY_BLUE = (0, 0, 128)
GRAY = (128, 128, 128)

# player settings
PLAYER_SPEED = 300
PLAYER_HIT_RECT = pg.Rect(0,0, TILESIZE-5, TILESIZE-5)