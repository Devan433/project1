import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Falling Blocks")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock
clock = pygame.time.Clock()

# Player settings
player_size = 50
player_pos = [WIDTH // 2, HEIGHT - player_size]

# Enemy settings
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

# Game loop
game_over = False
score = 0
font = pygame.font.SysFont("monospace", 35)

def detect_collision(player_pos, enemy_pos):
    px, py = player_pos
    ex, ey = enemy_pos
    return (
        ex < px + player_size and
        ex + enemy_size > px and
        ey < py + player_size and
        ey + enemy_size > py
    )

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= 10
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += 10

    enemy_pos[1] += enemy_speed
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1

    if detect_collision(player_pos, enemy_pos):
        game_over = True

    win.fill(WHITE)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    win.blit(text, (10, 10))

    pygame.draw.rect(win, BLUE, (*player_pos, player_size, player_size))
    pygame.draw.rect(win, RED, (*enemy_pos, enemy_size, enemy_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
