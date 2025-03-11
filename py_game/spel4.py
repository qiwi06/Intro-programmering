import pygame
import random

def collides(obj_1_x, obj_1_y, obj_1_radius, obj_2_x, obj_2_y, obj_2_radius):
    ''' Check if two objects collide. Circular collision detection.
    '''
    distance_squared = ((obj_1_x - obj_2_x) ** 2 + (obj_1_y - obj_2_y) ** 2)
    return distance_squared < (obj_1_radius + obj_2_radius) ** 2

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
size = (600, 600)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")

snake_image = pygame.image.load("py_game/img/snake.png")
snake_x = 50
snake_y = 500
snake_last_direction = "right"
snake_radius = (snake_image.get_width() + snake_image.get_height()) / 4

plum_image = pygame.image.load("py_game/img/plum.png")
plums = []
plum_radius = (plum_image.get_width() + plum_image.get_height()) / 4

score=0
font = pygame.font.Font(None,36)
text = font.render('Score=0', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (50,15)
 
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
            snake_x = 600
    if keys[pygame.K_RIGHT]:
        snake_x += 5
        if (snake_last_direction == "left"):
            snake_image = pygame.transform.flip(snake_image, True, False)
            snake_last_direction = "right"
        if snake_x > 600:
            snake_x = 0

    if (random.randint(0, 100) < 2):
        plum_x = random.randint(0, 600)
        plums.append([plum_x, 0, 0]) 
    
    for plum in plums:
        plum[1] += plum[2]
        plum[2] += 0.2
        if plum[1] > 800:
            plums.remove(plum)
        if collides(snake_x, snake_y, snake_radius, 
                    plum[0], plum[1], plum_radius):
            plums.remove(plum)
            score=score+1
            print("Yum!", score)
            text = font.render("Score="+str(score), True, BLACK, WHITE)
        
    screen.fill(GREEN)
 
    screen.blit(snake_image, [snake_x, snake_y])
    for plum in plums:
        screen.blit(plum_image, [plum[0], plum[1]])
    screen.blit(text, textRect)
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()