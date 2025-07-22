import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(25, 50)
        asteroid1_vel = self.velocity.rotate(angle)
        asteroid2_vel = self.velocity.rotate(-angle)
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position[0], self.position[1], new_rad)
        asteroid1.velocity = asteroid1_vel * 1.2
        asteroid2 = Asteroid(self.position[0], self.position[1], new_rad)
        asteroid2.velocity = asteroid2_vel * 1.2