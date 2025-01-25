#dont forget to activate the virutal environment: "source venv/bin/activate" ty !
import pygame
# I'd usually not import stuff like this but for a small and personal program it does not matter that much:
from constants import *
from player import *

def main():
    pygame.init()
    #set up a delta and a Clock for fps gestion
    dt = 0 
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2) # spawns the player in the middle of the screen
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #checks if the user closes the pygame tab, it will quit the game if they do
                return
        screen.fill((000,000,000))
        player.draw(screen)

        pygame.display.flip()
        #using the pygame.time.Clock.tick() function limits the fps to 60; Also save the time that past in millisecond in our delta value
        dt = clock.tick(60)/1000




if __name__ == "__main__":
    main()