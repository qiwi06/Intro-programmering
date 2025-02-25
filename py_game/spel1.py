#Import a library of functions called 'pygame'
import pygame

#Define some colors 
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()
#Open a window
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My Game")

#Add visual elements to the game
circle_x = 50 
circle_y = 50
circle_radius = 25
circle_speed_x = 10
circle_speed_y = 10

#Loop until the user clicks the close button.
done = False

#Used to manage how fast the screen updates. 
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    circle_x += circle_speed_x
    circle_y += circle_speed_y
    if circle_y > 475:
        circle_speed_y *= -1
    if circle_x >675:
        circle_speed_x *= -1
    if circle_y<0:
        circle_speed_y*=-1
    if circle_x<0:
        circle_speed_x*=-1

    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, [circle_x, circle_y], circle_radius)
    pygame.display.flip()
    clock.tick(60)
