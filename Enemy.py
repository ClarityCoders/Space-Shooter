import pygame
import random
from pygame import mixer
import math

def hit (ojb1x, obj1y, obj2x, obj2y):  
    dist = math.sqrt(math.pow(ojb1x-obj2x,2)+math.pow(obj1y-obj2y,2))
    if dist <34:
        return True
    else:        
        return False
    

class EnemyWave():
    def __init__(self, count):        
        self.enemy_list = []
        for i in range(count):
            self.enemy_list.append(Enemy())

    def check(self, screen, bullet, spaceship):
        score_tracker = 0
        for enemy in self.enemy_list:
            screen.blit(enemy.img, (int(enemy.x), int(enemy.y)))
            enemy.x += enemy.vel              
            enemy.y += .05
            if enemy.x > 440:
                enemy.vel = -(random.uniform(1,1))
            elif enemy.x < 0:
                enemy.vel = (random.uniform(1,1))    
            if bullet.shoot:
                test = hit(bullet.x,bullet.y,enemy.x,enemy.y)  
                if test:
                    bullet.shoot = False
                    contact = mixer.Sound("sounds/explosion.wav")
                    contact.set_volume(.5)
                    contact.play()
                    score_tracker += 1
                    enemy.x = random.randint(0, 500)
                    enemy.y = random.randint(10,250)    
                bullet.move(screen)
            if hit(spaceship.x, spaceship.y,enemy.x,enemy.y) or enemy.y > 350:
                return -1
        return score_tracker


class Enemy():

    img_list = ["images/ufo.png", "images/bigmonster.png"]
    
    def __init__(self):
        self.vel = 1
        self.x = random.randint(0,500)
        self.y = random.randint(10,250)
        self.img = pygame.image.load(Enemy.img_list[0])
