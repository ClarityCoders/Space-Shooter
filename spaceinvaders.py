import pygame
import random
import math
from pygame import mixer
from Spaceship import Spaceship
from Bullet import Bullet  


def hit (testx,testy,hitx,hity):  
    dist = math.sqrt(math.pow(hitx-bullet.x,2)+math.pow(hity-bullet.y,2))
    if dist <34:
        return True
    else:        
        return False
    

def game_intro():
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
              global runing
              runing = False
              intro = False
          
        screen.fill((255,255,255))
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

eme=["images/ufo.png","images/bigmonster.png"]
enemy_vel =[]
enemy_x =[]
enemy_y =[]
player2=[]
enemycount=10

clock = pygame.time.Clock()

for i in range(enemycount):
    enemy_vel.append(1)    
    enemy_x.append(random.randint(0,500))
    enemy_y.append(random.randint(10,250))
    if i % 2 == 0:    
        player2.append(pygame.image.load(eme[0]))
    else:
        player2.append(pygame.image.load(eme[1]))
    back=pygame.image.load("images/back.jpg")
   
game_intro()  
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

    for i in range(enemycount):
        if enemy_y[i]>=460:        
            showscore = font.render(f"Game over",True,(255,255,255))
            screen.blit(showscore,(250,250))
            if score > int(highscore) :
                highscore = score
                f = open("highscore.txt","w+")
                f.write(str(highscore))
                f.close()
            for j in range(enemycount):
                enemy_y[j] = 1000
        screen.blit(player2[i],(int(enemy_x[i]),int(enemy_y[i])))        
        enemy_x[i] += enemy_vel[i]              
        enemy_y[i] += .05
        if enemy_x[i] > 440:
           enemy_vel[i] = -(random.uniform(1,1))
        elif enemy_x[i] < 0:
           enemy_vel[i] =(random.uniform(1,1))    
        if bullet.shoot:
            test = hit(bullet.x,bullet.y,enemy_x[i],enemy_y[i])  
            if test:
                bullet.shoot = False
                contact = mixer.Sound("sounds/explosion.wav")
                contact.set_volume(.5)
                contact.play()
                score += 1
                enemy_x[i] = random.randint(0,500)
                enemy_y[i] = random.randint(10,250)    
            bullet.move(screen)
       
   
    pygame.display.update()
pygame.quit()