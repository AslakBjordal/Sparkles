import pygame
import random

SCREEN_X = 800
SCREEN_Y = 800
PARTICLE_IMAGE = "particle.png"
PARTICLES_PER_SECOND = 20
GRAVITY = 598.1

class Particle:
    def __init__(self, position, direction):
        self.position = pygame.math.Vector2(position)
        self.direction = pygame.math.Vector2(direction)
        self.image = pygame.image.load(PARTICLE_IMAGE).convert_alpha()

    def draw(self, screen):
        screen.blit(self.image, self.position)

    def move(self, time_passed):
        self.position += self.direction * time_passed
        self.direction.y += (GRAVITY  * time_passed)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_X,SCREEN_Y))
    particles = []
    clock = pygame.time.Clock()
    frame_counter = 0
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.USEREVENT:
                print("{} frames last second, with {} particles active".format(frame_counter, len(particles)))
                frame_counter = 0
            elif event.type == pygame.KEYDOWN:
                import pdb; pdb.set_trace()
        frame_counter += 1
        time_passed = clock.tick(200) / 1000.0

        for i in range(int(2000 * time_passed)):
            particles.append(Particle(
                            (SCREEN_X / 2, SCREEN_Y / 2), 
                            (random.randint(-100, 100), 
                            -random.random()*700.0)))

        screen.fill((0,0,0))
        for particle in particles:
            particle.move(time_passed)
            particle.draw(screen)
            if particle.position.y > SCREEN_Y:
                # Kanskje dette ikke er så lurt?
                particles.remove(particle)
        pygame.display.update()
