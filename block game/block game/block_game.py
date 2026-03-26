import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Player properties
player_pos = [WIDTH // 2, HEIGHT - 50]
player_size = 50

# Enemy properties
enemy_size = 50
enemy_pos = [random.randint(0, WIDTH - enemy_size), 0]
enemy_speed = 10

# Load enemy images and scale them
enemy_images = [
    pygame.transform.scale(pygame.image.load("download.jpg"), (enemy_size, enemy_size)),
    pygame.transform.scale(pygame.image.load("cat.png"), (enemy_size, enemy_size))
]
enemy_image_index = 0  # 0 for dog, 1 for cat

score = 0
game_over = False

# Screen shake variables
shake_frames = 0
SHAKE_DURATION = 10  # frames
SHAKE_INTENSITY = 20  # Increased intensity for testing

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_pos[0] -= 5  # Move left
    if keys[pygame.K_RIGHT]:
        player_pos[0] += 5  # Move right

    # Keep player within screen bounds
    player_pos[0] = max(0, min(WIDTH - player_size, player_pos[0]))

    # Update enemy position
    enemy_pos[1] += enemy_speed

    # --- CLOSE CALL DETECTION & SCREEN SHAKE ---
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    close_call_zone = pygame.Rect(player_pos[0], player_pos[1] - 20, player_size, player_size + 40)
    if (enemy_rect.colliderect(close_call_zone) and not player_rect.colliderect(enemy_rect)
        and enemy_pos[1] + enemy_size >= player_pos[1] and enemy_pos[1] < player_pos[1]):
        shake_frames = SHAKE_DURATION

    # --- ENEMY RESET & DYNAMIC DIFFICULTY ---
    if enemy_pos[1] > HEIGHT:
        enemy_pos[1] = 0
        enemy_pos[0] = random.randint(0, WIDTH - enemy_size)
        score += 1
        player_size += 5
        enemy_speed += 1
        player_pos[0] = min(player_pos[0], WIDTH - player_size)
        # Switch enemy image
        enemy_image_index = 1 - enemy_image_index
        print(f"Score: {score}, Enemy Speed: {enemy_speed}")

    # --- COLLISION DETECTION ---
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)
    enemy_rect = pygame.Rect(enemy_pos[0], enemy_pos[1], enemy_size, enemy_size)
    if player_rect.colliderect(enemy_rect):
        print("Game Over!")
        game_over = True

    # --- DRAWING WITH SCREEN SHAKE ---
    if shake_frames > 0:
        offset_x = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
        offset_y = random.randint(-SHAKE_INTENSITY, SHAKE_INTENSITY)
        shake_frames -= 1
    else:
        offset_x = 0
        offset_y = 0

    screen.fill((0, 0, 0))
    # Draw enemy image with shake offset
    screen.blit(enemy_images[enemy_image_index], (enemy_pos[0] + offset_x, enemy_pos[1] + offset_y))
    # Draw player as a blue rectangle with shake offset
    pygame.draw.rect(screen, BLUE, (player_pos[0] + offset_x, player_pos[1] + offset_y, player_size, player_size))

    pygame.display.update()
    clock.tick(30)

pygame.quit()
