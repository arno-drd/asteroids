#dont forget to activate the virutal environment: "source venv/bin/activate" ty !
import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                #checks if the user closes the pygame tab, it will quit the game if they do
                return
        screen.fill((000,000,000))
        pygame.display.flip()




if __name__ == "__main__":
    main()