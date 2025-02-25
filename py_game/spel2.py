import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Show text")
font = pygame.font.Font(None,36)
text = font.render('Alice', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (30,15)
done = False
clock = pygame.time.Clock()
nt= font.render('Rosa', True, BLACK, (254,134,164))
ntRect= nt.get_rect()
ntRect.center=(670,480)
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done= True
    screen.fill(RED)
    screen.blit(text, textRect)
    screen.blit(nt, ntRect)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()