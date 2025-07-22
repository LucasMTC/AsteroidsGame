import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(surface=screen, color="white", points=self.triangle(), width=2)
    
    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def update(self, dt):
        key = pygame.key.get_pressed()

        if key[pygame.K_a]:
            self.rotate(-dt)
        if key[pygame.K_d]:
            self.rotate(dt)
        if key[pygame.K_w]:
            self.move(dt)
        if key[pygame.K_s]:
            self.move(dt)
        if key[pygame.K_SPACE]:
            self.shoot()
        self.shot_timer -= dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shot_timer <= 0:
            shot = Shot(self.position[0], self.position[1])
            shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * SHOT_SPEED
            self.shot_timer = PLAYER_SHOT_COOLDOWN