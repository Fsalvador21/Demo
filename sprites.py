# Sprite Classes for pygame

import pygame as pg
import random
from settings import *
from pygame.sprite import Sprite
from time import *
vec = pg.math.Vector2

class Player(Sprite):
    def __init__(self, game):
        Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((30,40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH /2, HEIGHT /2)
        self.pos = vec(WIDTH / 2, HEIGHT /2)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        # self.vx = 0
        # self.vy = 0
        # self.acceleration = .5
        # self.falling = False
        # self.max_velocity = -25
    # Making jump possible
    def jump(self):
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
    # accerlation in Player
    def update(self):
        self.acc = vec(0, PLAYER_GRAV)

        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        # if keys[pg.K_UP] and self.falling = False
        #     self.jump()
        # if keys[pg.K_DOWN]:
        #     self.vy = 5

        # Friction applied(x-axis)
        self.acc.x += self.vel.x * PLAYER_FRCITION
        # Motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Sides wrap around
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos
    # def gravity(self):
    #     if self.rect.y < HEIGHT-40:
    #         self.falling = True
    #         self.vy += 10

# class Enemy(Sprite):
    # def __init__(self, game):
    #     Sprite.__init__(self)
    #     self.game = game
    #     self.image = pg.Surface((30,40))
    #     self.image.fill(PINKISH)
    #     self.rect = self.image.get_rect()
    #     self.rect.center = (WIDTH /2, HEIGHT /2)
    #     self.pos = vec(WIDTH / 2, HEIGHT /2)
    #     self.vel = vec(0, 0)
    #     self.acc = vec(0, 0)
    #     self.vx = 0
    #     self.vy = 0
    #     self.acceleration = .5
    #     self.falling = False
    #     self.max_velocity = -25
    
    # # Making jump possible
    # def jump(self):
    #     self.rect.x += 1
    #     hits = pg.sprite.spritecollide(self, self.game.platforms, False)
    #     self.rect.x -= 1
    #     if hits:
    #         self.vel.y = -20
    # # accerlation in Player
    # def update(self):
    #     self.acc = vec(0, PLAYER_GRAV)
    #     keys = pg.key.get_pressed()
    #     if keys[pg.K_a]:
    #         self.acc.x = -PLAYER_ACC
    #     if keys[pg.K_d]:
    #         self.acc.x = PLAYER_ACC
    #     # if keys[pg.K_UP] and self.falling = False
    #     #     self.jump()
    #     # if keys[pg.K_DOWN]:
    #     #     self.vy = 5

    #     # Friction applied(x-axis)
    #     self.acc.x += self.vel.x * PLAYER_FRCITION
    #     # Motion
    #     self.vel += self.acc
    #     self.pos += self.vel + 0.5 * self.acc
    #     # Sides wrap around
    #     if self.pos.x > WIDTH:
    #         self.pos.x = 0
    #     if self.pos.x < 0:
    #         self.pos.x = WIDTH

        # self.rect.midbottom = self.pos
    # def gravity(self):
        # if self.rect.y < HEIGHT-40:
        #     self.falling = True
        #     self.vy += 10

class Platforms(Sprite):
    def __init__(self, x, y, w, h):
        Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(PURPLE)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y