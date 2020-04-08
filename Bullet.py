import pygame
from pygame import mixer

class Bullet ():

    def __init__(self):        
        self.x = 250                
        self.y = 400
        self.shoot = False
        self.img = pygame.image.load("images/bullet.png")
        self.laser = mixer.Sound("sounds/laser.wav")

    def sound(self):
        self.laser.play()

    def check_move(self, event, ship_x, ship_y):
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not self.shoot:
                    self.sound()
                    self.x = ship_x
                    self.y = ship_y
                    self.shoot = True