import pygame
import random

# --- Define helper functions
def get_one_colliding_object(object_1, objects):
    '''Returns the first object in the list of objects
    that collides with object_1.
    Returns None if no object collides.'''
    for object_2 in objects:
        obj_1_rect = pygame.Rect(object_1['x'], object_1['y'], object_1['image'].get_width(), object_1['image'].get_height())
        obj_2_rect = pygame.Rect(object_2['x'], object_2['y'], object_2['image'].get_width(), object_2['image'].get_height())
        if obj_1_rect.colliderect(obj_2_rect):
            return object_2
    return None

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

sand_image = pygame.image.load("py_game/img/floor_sand_stone_0.png")
wall_image = pygame.image.load("py_game/img/brick_brown_0.png")
#door "img/open_door.png"
player_image = pygame.image.load("py_game/img/deep_elf_knight_old.png")
crystal_image = pygame.image.load("py_game/img/crystal_wall_lightmagenta.png")
crystals = []
# Lägga till monster
monster_image = pygame.image.load("py_game/img/phoenix.png")
monsters = []

# Add visual elements to the game

wall_size = wall_image.get_width()
walls = []

# Create the player
player = {}
player['image'] = player_image
player['speed'] = 4

score=0
font = pygame.font.Font(None,36)
text = font.render('Score=0', True, BLACK, WHITE)
textRect = text.get_rect()
textRect.center = (50, 15)
# Read the maze from the file.

file = open('py_game/maze.txt', 'r')
line = file.readline()
maze_width = len(line) - 1  # Do not count the newline character.
maze_height = 0
x = 0
y = 0
while len(line) > 1:
    maze_height += 1
    for char in line:
        if char == 'x' or char == 'd':
            wall = {}
            wall['x'] = x
            wall['y'] = y
            wall['image'] = wall_image
            walls.append(wall)
        elif char == 'e':
            player['x'] = x
            player['y'] = y
        elif char == 'm':
            monsters.append ({
                'x': x,
                'y': y,
                'image': monster_image,
                'direction': random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)]),
                'speed': 4
            })
        elif char == 'c':
            crystal = {}
            crystal['x'] = x
            crystal['y'] = y
            crystal['image'] = crystal_image
            crystals.append(crystal)
        x += wall_size
    x = 0
    y += wall_size
    line = file.readline()

file.close()

# --- Set the width and height of the screen [width, height]
size = (maze_width * wall_size, maze_height * wall_size)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Maze Game")
game_over = False

text2 = font.render('Score=0', True, BLACK, WHITE)
text2Rect = text2.get_rect()
text2Rect.center = (50, 15)
# --- Game time
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
is_running = True
while is_running:
    # --- Event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False
    # --- Game logic should go here
    # --- Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player['x'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] += player['speed']

    elif keys[pygame.K_RIGHT]:
        player['x'] += player['speed']
        if get_one_colliding_object(player, walls):
            player['x'] -= player['speed']
    elif keys[pygame.K_DOWN]:
        player['y'] += player['speed']
        if get_one_colliding_object(player, walls):
            player['y'] -= player['speed']
    elif keys[pygame.K_UP]:
        player['y'] -= player['speed']
        if get_one_colliding_object(player, walls):
            player['y'] += player['speed']

    else:
        # snap player to grid
        player['x'] = round(player['x'] / wall_size) * wall_size
        player['y'] = round(player['y'] / wall_size) * wall_size

    # collision with crystals?
    crystal = get_one_colliding_object(player, crystals)
    if crystal:
        crystals.remove(crystal)
        score=score+1
        print("Kristaller fångade:", score)
    text = font.render("Score="+str(score), True, BLACK, WHITE)

    # flytta monster
    for monster in monsters:
        # för varje monster gör ...
        # gå nedåt, stopp vid vägg, sedan vänster eller höger
        # NER
        if monster['direction']==(0, 1):
            #ner           
            monster['y'] += monster['speed']
        if get_one_colliding_object(monster, walls):
            monster['y'] -= monster['speed']
            # ny riktning
            monster['direction'] = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        # UPP
        if monster['direction']==(0,-1):
            monster['y'] -= monster['speed']
        if get_one_colliding_object(monster, walls):
            monster['y'] += monster['speed']
            monster['direction'] = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        # Höger
        if monster['direction']==(1,0):
            monster['x'] += monster['speed']
        if get_one_colliding_object(monster,walls):
            monster['x'] -= monster['speed']
            monster['direction'] = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        # Vänster
        if monster['direction']==(-1,0):
            monster['x'] -= monster['speed']
        if get_one_colliding_object(monster,walls):
            monster['x'] += monster['speed']
            monster['direction'] = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])

            
    if get_one_colliding_object(player, monsters):
        # game over
        print("Game over!")
        text2 = font.render("Game over!", True, BLACK, WHITE)
        is_running = False




    # --- Screen-clearing code goes here
    # fill widh san
    for y in range(0, size[1], wall_size):
        for x in range(0, size[0], wall_size):
            screen.blit(sand_image, (x, y))
    # --- Drawing code should go here
    for wall in walls:
        screen.blit(wall_image, (wall['x'], wall['y']))
    screen.blit(player_image, (player['x'], player['y']))
    # Rita upp monster
    for monster in monsters:
        screen.blit(monster_image, (monster['x'], monster['y']))
    for crystal in crystals:
        screen.blit(crystal_image, (crystal['x'], crystal['y']))
    screen.blit(text, textRect)
    

    
    pygame.display.update()  # or pygame.display.flip()
    # --- Increase game time
    clock.tick(60)  # 60 frames per second

# Clean up when the game exits.
pygame.quit()