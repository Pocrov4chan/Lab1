import pygame 
import sys
import random

pygame.init()

# Some constants
# Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ANOTHER_GREEN = (0, 100, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH = 800
HEIGHT = 800
CELL_SIZE = 40

FONT = pygame.font.SysFont("Verdana", 35)

# Screen info
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake_game")

FPS = 5
clock = pygame.time.Clock()

# Creating our class "Snake"
class Snake:
    def __init__(self):
        self.x = CELL_SIZE
        self.y = CELL_SIZE
        self.xdirection = 1
        self.ydirection = 0
        self.head = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        self.body = [pygame.Rect(self.x - CELL_SIZE, self.y, CELL_SIZE, CELL_SIZE)]
        self.dead = False

    def update(self):
        global apple
        global FPS
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.dead = True
            if self.head.x not in range(0, WIDTH) or self.head.y not in range(0, HEIGHT):
                self.dead = True

        #check whether the snake is dead or no
        if self.dead:
            self.x = CELL_SIZE
            self.y = CELL_SIZE
            self.xdirection = 1
            self.ydirection = 0
            self.head = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
            self.body = [pygame.Rect(self.x - CELL_SIZE, self.y, CELL_SIZE, CELL_SIZE)]
            self.dead = False
            apple = Apple()
            FPS = 5

        # logic behind eating the apple
        self.body.append(self.head)
        for i in range(0, len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i + 1].x, self.body[i + 1].y
        self.head.x += self.xdirection * CELL_SIZE
        self.head.y += self.ydirection * CELL_SIZE
        self.body.remove(self.head)

#We define our class Apple
class Apple:
    def __init__(self):
        self.generate_food()

    def generate_food(self):
        self.x = int(random.randint(0, WIDTH) / CELL_SIZE) * CELL_SIZE
        self.y = int(random.randint(0, HEIGHT) / CELL_SIZE) * CELL_SIZE
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)

    def update(self):
        pygame.draw.rect(screen, RED, self.rect)

#define class for randomly occuring event "SpecialApple"
class SpecialApple(Apple):
    def __init__(self):
        super().__init__()
        self.visible = False
        self.timer = 0

    def generate_food(self):
        self.x = int(random.randint(0, WIDTH) / CELL_SIZE) * CELL_SIZE
        self.y = int(random.randint(0, HEIGHT) / CELL_SIZE) * CELL_SIZE
        self.rect = pygame.Rect(self.x, self.y, CELL_SIZE, CELL_SIZE)
        self.visible = True
        self.timer = 0

    def update(self):
        if self.visible:
            pygame.draw.rect(screen, BLUE, self.rect)

def draw_grid():
    for x in range(0, WIDTH, CELL_SIZE):
        for y in range(0, HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

score = FONT.render("1", True, WHITE)
score_rect = score.get_rect(center=(55, 50))

SPECIAL_APPLE = pygame.USEREVENT + 1
pygame.time.set_timer(SPECIAL_APPLE, 20000)

#Creating objects
draw_grid()

snake = Snake()

apple = Apple()
special_apple = SpecialApple()

apples_eaten = 0

#Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        #movement of the snake
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydirection = 1
                snake.xdirection = 0
            elif event.key == pygame.K_UP:
                snake.ydirection = -1
                snake.xdirection = 0
            elif event.key == pygame.K_LEFT:
                snake.ydirection = 0
                snake.xdirection = -1
            elif event.key == pygame.K_RIGHT:
                snake.ydirection = 0
                snake.xdirection = 1
        if event.type == SPECIAL_APPLE:
            special_apple.generate_food()

    snake.update()

    screen.fill(BLACK)
    draw_grid()

    apple.update()
    # logic behind special apple
    if special_apple.visible:
        special_apple.update()
        special_apple.timer += 1
        if special_apple.timer > 50:
            special_apple.visible = False

    score = FONT.render(f"Score: {len(snake.body) - 1} Level: {(len(snake.body) - 1) // 3}", True, WHITE)

    pygame.draw.rect(screen, ANOTHER_GREEN, snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, GREEN ,square)

    screen.blit(score, score_rect)

    #collisions
    if snake.head.colliderect(apple.rect):
        snake.body.append(pygame.Rect(square.x, square.y, CELL_SIZE, CELL_SIZE))
        apple.generate_food()
        apples_eaten += 1
        if apples_eaten % 3 == 0:  # Level up every 3 apples eaten
            FPS += 1  # Increase speed

    if snake.head.colliderect(special_apple.rect):
        snake.body.append(pygame.Rect(square.x, square.y, CELL_SIZE, CELL_SIZE))
        snake.body.append(pygame.Rect(square.x, square.y, CELL_SIZE, CELL_SIZE))
        snake.body.append(pygame.Rect(square.x, square.y, CELL_SIZE, CELL_SIZE))
        special_apple.generate_food()
        apples_eaten += 3
        FPS += 1

    clock.tick(FPS)        
    pygame.display.update()
