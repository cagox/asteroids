# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

updateable = pygame.sprite.Group()
drawable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()
Player.containers = (updateable, drawable)
Asteroid.containers = (asteroids, updateable, drawable)
AsteroidField.containers = (updateable,)
Shot.containers = (updateable, shots, drawable)

def main():
    score = 0
    pygame.init()
    pygame.display.set_caption(PYGAME_DISPLAY_NAME)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    font = pygame.font.Font('freesansbold.ttf', 32)

    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        score_text = font.render(str(score), True, "white")
        score_rect = score_text.get_rect()
        score_rect.top = 10
        score_rect.left = 10

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0,0,0))
        screen.blit(score_text, score_rect)

        dt = clock.tick(60)/1000
        updateable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if shot.collides(asteroid):
                    shot.kill()
                    score += 1
                    asteroid.split()

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game Over")
                print(f"Score: {score}")
                exit()
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()

    # print("Starting asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()


