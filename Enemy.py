import math
import pygame
import random
from pygame import mixer

def hit (ojb1x, obj1y, obj2x, obj2y):  
    dist = math.sqrt(math.pow(ojb1x-obj2x, 2)+math.pow(obj1y-obj2y, 2))
    if dist < 34:
        return True
    else:        
        return False

class EnemyWave():
    def __init__(self, count):        
        self.enemy_list = []
        for i in range(count):
            self.enemy_list.append(Enemy(self.enemy_list))

    def check(self, screen, bullet, spaceship, speed):
        score_tracker = 0
        for enemy in self.enemy_list:
            screen.blit(enemy.img, (int(enemy.x), int(enemy.y)))
            if enemy.x > 500 - enemy.img.get_rect().size[0] or enemy.x <= 0:
                enemy.velx *= -1  
            enemy.x += enemy.velx * speed
            enemy.y += enemy.vely * speed
            if bullet.shoot:
                test = hit(bullet.x,bullet.y,enemy.x,enemy.y)  
                if test:
                    bullet.shoot = False
                    contact = mixer.Sound("sounds/explosion.wav")
                    contact.set_volume(.5)
                    contact.play()
                    score_tracker += 1
                    enemy.new_location(self.enemy_list)
                    enemy.speed_up()
                bullet.move(screen)
            if hit(spaceship.x, spaceship.y, enemy.x, enemy.y) or enemy.y > 500:
                print(f'Loss ---- \nSpaceship: {spaceship.x}, {spaceship.y} \nEnemy: {enemy.x},{enemy.y}')
                return -1
        return score_tracker


class Enemy():
    img_list = [pygame.image.load("images/ufo.png"), pygame.image.load("images/bigmonster.png")]
    
    def __init__(self, enemy_list):
        self.velx = 10
        self.vely = 1
        self.img = Enemy.img_list[0]
        self.new_location(enemy_list)

    def new_location(self, enemy_list):
        new_spot = True
        while new_spot:
            new_spot = False
            holder_x = random.randint(1, 500 - self.img.get_rect().size[0])
            holder_y = random.randint(10, 250)
            for enemy in enemy_list:
                new_spot = hit(holder_x, holder_y, enemy.x, enemy.y)
                if new_spot:
                    break
        self.x = holder_x
        self.y = holder_y

    def speed_up(self):
        if abs(self.velx) > 30:
            self.vely *= 1.5
        else:
            self.velx *= 1.5
