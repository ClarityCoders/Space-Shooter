import pygame
import random

class EnemyWave():
    def __init__(self, count):        
        self.enemy_list = []
        for i in range(count):
            self.enemy_list.append(Enemy())

class Enemy():

    img_list = ["images/ufo.png", "images/bigmonster.png"]
    
    def __init__(self):
        self.vel = 1
        self.x = random.randint(0,500)
        self.y = random.randint(10,250)
        self.img = pygame.image.load(Enemy.img_list[0])
