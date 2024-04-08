import pygame
import sys
import random
import time

# Initialising of the pygame
pygame.init()

# frame rate of our application
FPS = 60
FramePerSec = pygame.time.Clock()

score_control = 5

# Predefined constants
SPEED = 5
SCORE = 0
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Fonts
font_main = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font_main.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

# Screen Information
WIDTH = 400
HEIGHT = 600

DISPLAY_SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))
DISPLAY_SURFACE.fill(WHITE)
pygame.display.set_caption("Racer")

# Initializing class for enemy
class Enemy(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)

    # movement method
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if(self.rect.top > HEIGHT):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

# Initializing class for Player
class Player(pygame.sprite.Sprite):
    # Constructor
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    # movement method
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            if (self.rect.left > 0):
                self.rect.move_ip(-5, 0)

        if pressed_keys[pygame.K_RIGHT]:
            if (self.rect.right < WIDTH):
                self.rect.move_ip(5, 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self, coin_type, worth):
        super().__init__()
        self.image = pygame.image.load(coin_type)
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0)
        self.worth = worth

    def move(self):
        global SCORE, SPEED, score_control
        if SCORE > score_control:
            SPEED += 1
            score_control += 5
        self.rect.move_ip(0, SPEED)


# Objects
P1 = Player()
E1 = Enemy()

# Groups
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()

# Adding a new User event
COIN_CREATION = pygame.USEREVENT + 1
pygame.time.set_timer(COIN_CREATION, 3000)

# Main loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == COIN_CREATION:
            rand_number = random.randint(1,3)
            if rand_number == 1:
                coin = Coin("coin_1.png", 1)
            elif rand_number == 2:
                coin = Coin("coin_2.png", 3)
            else:
                coin = Coin("coin_3.png", 5)
            coins.add(coin)

    DISPLAY_SURFACE.blit(background, (0,0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAY_SURFACE.blit(scores, (10,10))

    for sprite in all_sprites:
        DISPLAY_SURFACE.blit(sprite.image, sprite.rect)
        sprite.move()

    for coin in coins:
        DISPLAY_SURFACE.blit(coin.image, coin.rect)
        coin.move()

    # Check for collisions between player and coins
    coin_collisions = pygame.sprite.spritecollide(P1, coins, True)
    for coin in coin_collisions:
        SCORE += coin.worth

    #collision logic
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)

        DISPLAY_SURFACE.fill(RED)
        DISPLAY_SURFACE.blit(game_over, (30,250))

        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
