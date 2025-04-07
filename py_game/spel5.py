import pygame

RED = (255, 0, 0)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)
BLUE = (0, 0, 255)

pygame.init()

size = (800, 600)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Collision with Walls")

bird_image = pygame.image.load("py_game/img/pelican.png")
bird_x = 0
bird_y = 0
bird_last_direction = "right"

# Box
# Green but red when there is a collision.
box = pygame.Rect(100, 100, 200, 200)
box_color = GREEN

box2 = pygame.Rect(500, 500, 100, 50)
box2_color = BLUE

is_running = True
# Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    # --- Game logic should go here
    # Move the bird with the arrow keys.
    
    # ... Write code here ....
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bird_x -= 5
        if box.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_x += 5
        if box2.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_x += 5
        if (bird_last_direction == "right"):
            bird_image = pygame.transform.flip(bird_image, True, False)
            bird_last_direction = "left"
        if bird_x < 0:
            bird_x = 800
    if keys[pygame.K_RIGHT]:
        bird_x += 5
        if box.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_x -= 5
        if box2.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_x -= 5
        if (bird_last_direction == "left"):
            bird_image = pygame.transform.flip(bird_image, True, False)
            bird_last_direction = "right"
        if bird_x > 800:
            bird_x = 0
    if keys[pygame.K_UP]:
        bird_y -= 5
        if box.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_y += 5
        if box2.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_y += 5
        if (bird_last_direction == "down"):
            bird_image = pygame.transform.flip(bird_image, True, False)
            bird_last_direction = "down"
        if bird_y < 0:
            bird_y = 600
    if keys[pygame.K_DOWN]:
        bird_y += 5
        if box.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_y -= 5
        if box2.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
            bird_y -= 5
        if (bird_last_direction == "up"):
            bird_image = pygame.transform.flip(bird_image, True, False)
            bird_last_direction = "up"
        if bird_y > 600:
            bird_y = 0

    # Check for collision between the bird and the box.
    if box.colliderect(bird_image.get_rect(topleft=(bird_x, bird_y))):
        box_color = RED
    else:
        box_color = GREEN

    # --- Screen-clearing code goes here
    screen.fill(SKY_BLUE)
    # --- Drawing code should go here
    screen.blit(bird_image, (bird_x, bird_y))
    pygame.draw.rect(screen, box_color, box)
    pygame.draw.rect(screen, box2_color, box2)
    pygame.display.update()  # or pygame.display.flip()
    # --- Increase game time
    clock.tick(60)  # 60 frames per second

# Clean up when the game exits.
pygame.quit()