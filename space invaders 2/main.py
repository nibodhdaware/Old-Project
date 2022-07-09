# importing libraries
import pygame
import random
import os
import time
pygame.font.init()

WIDTH, HEIGHT = 700, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders 2")

# load images
RED_SPACE_SHIP = pygame.image.load(
    os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(
    os.path.join('assets', "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(
    os.path.join('assets', "pixel_ship_blue_small.png"))

# PLAYER
YELLOW_SPACE_SHIP = pygame.image.load(
    os.path.join('assets', "pixel_ship_yellow.png"))

# lasers
RED_LASERS = pygame.image.load(os.path.join('assets', "pixel_laser_red.png"))
GREEN_LASERS = pygame.image.load(os.path.join('assets', "pixel_laser_red.png"))
BLUE_LASERS = pygame.image.load(os.path.join('assets', "pixel_laser_red.png"))
YELLOW_LASERS = pygame.image.load(
    os.path.join('assets', "pixel_laser_red.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(
    os.path.join('assets', "background-black.png")), (WIDTH, HEIGHT))


class Ship:

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0

    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))

    def get_width(self):
        return self.ship_img.get_width()

    def get_height(self):
        return self.ship_img.get_height()


class Player(Ship):
    def __init__(self, x, y, health=100):
        super().__init__(x, y, health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASERS
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health


class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASERS),
        "green": (GREEN_SPACE_SHIP, GREEN_LASERS),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASERS)
    }

    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self, vel):
        self.y += vel


def main():
    run = True
    FPS = 60
    level = 0
    lives = 5
    ship = Player(250, 500)
    main_font = pygame.font.SysFont("comicsans", 50)
    clock = pygame.time.Clock()
    ship_vel = 5
    enemies = []
    wave = 5
    enemy_vel = 1

    def redraw_window():
        WIN.blit(BG, (0, 0))
        # draw
        level_label = main_font.render(f'Level: {level}', 1, (255, 255, 255))
        lives_label = main_font.render(f'Lives: {lives}', 1, (255, 255, 255))

        WIN.blit(lives_label, (10, 10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        ship.draw(WIN)
        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if len(enemies) == 0:
            level += 1
            wave += 2
            for i in range(wave):
                enemy = Enemy(random.randrange(
                    50, WIDTH - 100), random.randrange(-1500, -100), random.choice(["red", "green", "blue"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x - ship_vel > 0:
            ship.x -= ship_vel
        if keys[pygame.K_d] and ship.x + ship_vel + ship.get_width() < WIDTH:
            ship.x += ship_vel
        if keys[pygame.K_w] and ship.y - ship_vel > 0:
            ship.y -= ship_vel
        if keys[pygame.K_s] and ship.y + ship_vel + ship.get_height() < HEIGHT:
            ship.y += ship_vel

        for enemy in enemies:
            enemy.move(enemy_vel)


main()
