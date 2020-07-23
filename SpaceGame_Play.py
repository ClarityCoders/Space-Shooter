import pygame
from Spaceship import Spaceship
from Bullet import Bullet
from Enemy import EnemyWave

pygame.init()
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
BACKGROUND = back = pygame.image.load("images/back.jpg")


def draw_screen(screen, score, highscore, bullet, spaceship):
    screen.fill((0, 0, 0))
    screen.blit(BACKGROUND, (0, 0))
    font = pygame.font.SysFont("comicsans", 40)
    showscore = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(showscore, (SCREEN_WIDTH - 10 - showscore.get_width(), 10))              
    showscore = font.render(f"High Score: {highscore}", True, (255, 255, 255))
    screen.blit(showscore, (10, 10))
    bullet.show(screen)
    spaceship.show(screen)


def main():
    # create our screen
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Check for a highscore file if not set to 0
    try:
        f = open("highscore.txt", "r")
        highscore = int(f.readline())
        f.close()
    except:
        highscore = 0

    spaceship = Spaceship()
    bullet = Bullet()

    score = 0
    running = True

    clock = pygame.time.Clock()
    enemy_wave = EnemyWave(5, spaceship)
    while running:
        clock.tick(30)
        draw_screen(screen, score, highscore, bullet, spaceship)
        
        spaceship.move(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            spaceship.check_move(event)
            bullet.check_move(event, spaceship.x, spaceship.y)

        result = enemy_wave.check(screen, bullet, spaceship)
        if result >= 0:
            score += result
        else:
            running = False
            if score > int(highscore):
                f = open("highscore.txt", "w")
                f.write(str(score))
                f.close()

        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
