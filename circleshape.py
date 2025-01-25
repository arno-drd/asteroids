import pygame

# the class we are using to create asteroids and hitboxes
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        """to be overrided by child classes"""
        pass

    def update(self, dt):
        """to be overrided by child classes"""
        pass

    def collision(self, target):
        """returns True if colliding with the target"""
        return self.position.distance_to(target.position) < self.radius + target.radius