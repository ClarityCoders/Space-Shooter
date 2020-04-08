import pygame

class Spaceship ():
    def __init__(self):
        self.vel = 10
        self.x = 250
        self.y = 400
        self.move_x = 0
        self.move_y = 0
        self.img = pygame.image.load("images/spaceship.png")

    def check_move(self, event, speed):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and self.x > self.vel:
                self.move_x -= self.vel * speed
            if event.key == pygame.K_RIGHT and self.x < 500 - 64 - self.vel :
                self.move_x += self.vel * speed
            if event.key == pygame.K_UP and self.y > self.vel :
                self.move_y -= self.vel * speed
            if event.key == pygame.K_DOWN and self.y < 500 - 64 - self.vel:
                self.move_y += self.vel * speed
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                self.move_x = 0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                self.move_y = 0

    def move(self, screen):
        self.x += self.move_x
        self.y += self.move_y
        screen.blit(self.img,(int(self.x),int(self.y)))