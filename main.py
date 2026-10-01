# File created by: Tarun Venkat
# Content inspired by: Chris Bradfield
# I do solemnly swear to create concise and informative comments

"""
The game engine consists of three (four) basic components:

Input - keys, buttons, voice, mouse, touch, breath, movement, control stick
Process - input processed (direction of control, magnitude)
Output - draw new pixels, sound, haptic (senses)
(Store)
"""

import pygame as pg
from os import path
from settings import *
from sprites_coz1 import *
from utils import *

# Game class (a blueprint for entire game).
class Game:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))

        #ensure class is initialized
        print("game class initialized")
        self.clock = pg.time.Clock()
        self.running = True
        self.playing = True

    #physically load map info from map file
    def load_data(self, map):
        self.game_dir = path.dirname(__file__)
        self.img_dir = path.join(self.game_dir, 'images')
        self.map = Map(path.join(self.game_dir, map))

    #make a new level and screen
    def new(self):
        self.load_data('level1.txt')
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()

        #instantiate player and read wall data here
        self.wall = Wall(self, 0, 10)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    Player(self, col, row)
                
    #physically run code
    def run(self):
        self.load_data('level1.txt')
        while self.running:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()  #gets player input.
            self.update()  #updates the game.
            self.draw()  #creates sprites.

    #determine whether to 
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

    #refreshes the screen and anything drawn.
    def update(self):
        self.all_sprites.update()

    #actually draws the objects.
    def draw(self):
        self.screen.fill(BLUE)
        self.all_sprites.draw(self.screen)

        pg.display.flip()

#run game loop
if __name__ == "__main__":
    g = Game()
    while g.running:
        g.new()
        g.run()

    pg.quit()
