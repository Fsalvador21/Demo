# This file was created by Fernando Salvador Francisco
# Thanks to Chris Bratfield from Kids can Code

import pygame as pg
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # init game window, try:
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("Cube Jumps")
        self.clock = pg.time.Clock()
        self.running = True
        # init pygame and create...
    def new(self):
        self.all_sprites = pg.sprite.Group()
        # Platform group
        self.platforms = pg.sprite.Group()
        # Adding player
        self.player = Player(self)
        self.all_sprites.add(self.player)
        # instantiate new platforms
        for plat in PLATFORM_LIST:
            p = Platforms(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        # run method
        self.run()
        # create new player object
    def run(self):
        self.playing = True
        # game loop
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
            
    def update(self):
        self.all_sprites.update()
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
        # print(hits)
            if hits:
                self.player.pos.y = hits[0].rect.top + 1
                self.player.vel.y = 0
                #scroll platform with player
        if self.player.rect.top <= HEIGHT / 4:
            self.player.pos.y += abs(self.player.vel.y)
            for plat in self.platforms:
                plat.rect.y += abs(self.player.vel.y)
                if plat.rect.top >= HEIGHT + 40:
                    plat.kill()
        if len(self.platforms) < 6:
            width = random.randrange(50, 100)
            p = Platforms(random.randrange(0, WIDTH-width),
                        random.randrange(-75, -30),
                        width, 20)
            self.platforms.add(p)
            self.all_sprites.add(p)   
        # update game

    
    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()   
        # listening for events
        # Applying jump

    def draw(self):
        self.screen.fill(PINK)
        self.all_sprites.draw(self.screen)
        # double buffer
        pg.display.flip()
        
    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass


g = Game()
g.show_start_screen()
while g.running: 
    g.new()
    g.show_go_screen