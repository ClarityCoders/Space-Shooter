import pygame


class Spaceship():
    def __init__(self):
        self.vel = 40
        self.x = 250
        self.y = 400
        self.move_x = 0
        self.move_y = 0
        self.img = pygame.image.load("images/spaceship.png")
        self.image_mask = pygame.mask.from_surface(self.img)

    def check_move(self, event, speed):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.move_x -= self.vel * speed
            if event.key == pygame.K_RIGHT:
                self.move_x += self.vel * speed
            if event.key == pygame.K_UP:
                self.move_y -= self.vel * speed
            if event.key == pygame.K_DOWN:
                self.move_y += self.vel * speed
        if event.type == pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                self.move_x = 0
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                self.move_y = 0

    def move(self, screen):
        width_bound = 500 - self.img.get_rect().size[0]
        height_bound = 500 - self.img.get_rect().size[1]

        if self.x + self.move_x < width_bound and self.x + self.move_x > 0:
            self.x += self.move_x
        if self.y + self.move_y < height_bound and self.y + self.move_y > 0:
            self.y += self.move_y
        screen.blit(self.img, (int(self.x),int(self.y)))