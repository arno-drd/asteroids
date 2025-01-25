import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        """overrides the draw method from CircleShape()"""
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius == ASTEROID_MIN_RADIUS :
            return
        new_angle = random.uniform(20, 50)
        