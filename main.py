import pygame
from asteroidfield import AsteroidField
from constants import *
from player import Player
from asteroid import Asteroid

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    dt = 0
    clock = pygame.time.Clock()
   

    #groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    asteroid_field = AsteroidField()
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for item in updatable:
            item.update(dt)
        for asteroid in asteroids:
            if asteroid.collision(player):
                print("Game over!")
                pygame.event.post(pygame.event.Event(pygame.QUIT))
        screen.fill("black")
        for item in drawable:
            item.draw(screen)
    
        pygame.display.flip()
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()