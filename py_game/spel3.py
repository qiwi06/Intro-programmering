import pygame
 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
size = (400, 400)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("The Snake Game")

snake_image = pygame.image.load("img/snake.png")
snake_x = 50
snake_y = 300
snake_last_direction = "right"

clock = pygame.time.Clock()

is_running = True

while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        snake_x -= 5
        if (snake_last_direction == "right"):
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_last_direction = "left"
        if snake_x < 0:
            snake_x = 400
    screen.fill(GREEN)
 
    screen.blit(snake_image, [snake_x, snake_y])
 
    pygame.display.flip()
    clock.tick(60)