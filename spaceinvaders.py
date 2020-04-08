import pygame
import random
import math
from pygame import mixer
from Spaceship import Spaceship
from Bullet import Bullet
from Enemy import EnemyWave
from Enemy import Enemy

def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              global runing
              runing = False
              intro = False
          
        screen.fill((255, 255, 255))
        font = pygame.font.SysFont("normalname.ttf",32) 
        message = font.render(f"Our Game",True,(0,0,0))
        screen.blit(message,(10,10))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        
        if 50 + 100 > mouse[0] > 100 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(screen, (0,255,0), (50,350,100,50))
            if click[0] == 1:
                print("hey")
                intro = False
        else:
            pygame.draw.rect(screen, (0,200,0), (50,350,100,50))
        
        if 250 + 100 > mouse[0] > 250 and 350 + 50 > mouse[1] > 350:
            pygame.draw.rect(screen, (255,0,0), (250,350,100,50))
        else:
            pygame.draw.rect(screen, (200,0,0), (250,350,100,50))
        
        
        pygame.display.update() 


pygame.init()

highscore = 0
f=open("highscore.txt", "r")
highscore = f.readline()
f.close()

spaceship = Spaceship()  
bullet = Bullet()

score = 0
font = pygame.font.SysFont("normalname.ttf", 32)  
fontx = 10  
fonty = 10

screen = pygame.display.set_mode((500, 500))
global runing
runing = True

clock = pygame.time.Clock()

back = pygame.image.load("images/back.jpg")
   
enemy_wave = EnemyWave(10)

#game_intro()  
while runing:
    dt = clock.tick(60)
    speed = 1 / float(dt)
    screen.fill((0,0,0))
    screen.blit(back,(0,0))
    
    spaceship.move(screen) 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runing=False
        spaceship.check_move(event, speed)
        bullet.check_move(event, spaceship.x, spaceship.y)
                   
    showscore = font.render(f"Score: {score}",True,(255,255,255))
    screen.blit(showscore,(fontx,fonty))              
    showscore = font.render(f"High Score: {highscore}",True,(255,255,255))
    screen.blit(showscore,(290,fonty))              

    result = enemy_wave.check(screen, bullet)
    score += result

    pygame.display.update()
pygame.quit()