import pygame
from pygame import mixer

class Bullet ():
    
    def __init__(self):        
        self.x = 250                
        self.y = 400
        self.img = pygame.image.load("images/bullet.png")
        self.laser = mixer.Sound("sounds/laser.wav")

    def sound(self):
        self.laser.play()