import pygame
from pygame import mixer

class Enemy():

    def __init__(self):        
        self.enemy_vel = []
        self.enemy_x = []
        self.enemy_y = []
        self.queue= []
        self.enemycount = 10
        self.img = ["images/ufo.png", "images/bigmonster.png"]