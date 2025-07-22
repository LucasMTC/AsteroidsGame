import pygame
import math

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
        pass

    def update(self, dt):
        pass

    def colide(self, object):
        if math.sqrt(abs(self.position[1] - object.position[1])**2 + abs(self.position[0] - object.position[0])**2) <= object.radius + self.radius:
            return True
        return False