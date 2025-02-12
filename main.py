#dont forget to activate the virutal environment: "source venv/bin/activate" ty !
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroid_field import AsteroidField
from shoot import Shot

def main():
    """Initialize and run the main game loop."""
    pygame.init()
    #set up a delta and a Clock for fps gestion
    dt = 0 
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #setting up groups so the code is optimal wwhen we will add a lot of other objects that will update and draw, in the infinite loop of the game
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # spawns the player in the middle of the screen
    
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField() #creates the asteroid fields, spawns asteroids randomly when updated

    Shot.containers = (shots, updatable, drawable)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #checks if the user closes the pygame tab, it will quit the game if they do
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids :
            if asteroid.collision(player) :
                print("Game Over !")
                sys.exit()
            for shot in shots :
                if asteroid.collision(shot):
                    asteroid.split()
                    shot.kill()
        screen.fill((000,000,000))

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        #using the pygame.time.Clock.tick() function limits the fps to 60; Also save the time that past in millisecond in our delta value
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()