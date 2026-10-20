# File created by: Tarun Venkat
# Content inspired by: Chris Bradfield
# I do solemnly swear to create concise and informative comments

"""
The game engine consists of three (four) basic components:

Input - keys, buttons, voice, mouse, touch, breath, movement, control stick
Process - input processed (direction of control, magnitude)
Output - draw new pixels, sound, haptic (senses)
(Store)

GOALS: get to a shark character
RULES: time limit, no touching cup enemies
FEEDBACK: screen turns red if touching enemy, gold if touching target
FREEDOM: movement within walls, ability to touch enemies or targets
"""

import pygame as pg
from os import path
from settings import *
from sprites import *
from utils import *

# Game class (blueprint for entire game).
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
        self.player.coins = 0
        self.score = 0
        self.highscore = 0 

    #physically load map info from map file
    def load_data(self, map):
        self.game_dir = path.dirname(__file__)
        self.game_save_dir = path.join(self.game_Dir,"example.txt")
        self.img_dir = path.join(self.game_dir, 'images')
        self.snd_dir = path.join(self.game_dir, 'sounds')
        self.map = Map(path.join(self.game_dir, map))

        # see if fie exists, create if not
        try:
            with open(self.game_save_dir, "x", encoding ="utf=8") as file:
                file.write("Hello World!")
            print("File created succesfully")
        except FileExistsError:
            print("File already exists, no action taken.")

        # open file and try to set high score with except set high score to zero
        with open(self.game_save_dir, 'r') as f:
            try:
                self.highscore = int(f.read())
                print("High score set!")
            except:
                self.highscore = 0
                print("high score is zero")
    
    #make a new level and screen
    def new(self):
        self.load_data('level1.txt')
        self.all_sprites = pg.sprite.Group()
        self.all_walls = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_coins = pg.sprite.Group()

        #instantiate player
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row)
                if tile == 'M':
                    Mob(self, col, row)
                if tile == 'C':
                    Coin(self, col, row)
        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    Player(self, col, row)
                
    #physically run code
    def run(self):
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
        self.draw_text("fps: "+str(floor(1/self.dt)),24, WHITE, WIDTH/2, HEIGHT/4)
        self.draw_text(f"coins: {self.player.coins}",24, WHITE, WIDTH/2, HEIGHT/9)
        pg.display.flip()

    #draw text on screen anywhere
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

#run game loop
if __name__ == "__main__":
    g = Game()

while g.running:
    g.new()
    g.run()

pg.quit()
