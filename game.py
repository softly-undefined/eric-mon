import pygame
import settings
import maps


#Eric Bennett, 2/20/24
# this is a super fun project!!!
# going for just below pokemon gen 3 quality (so cool how complex that game is)
#
#
# slow the player down!! need to have running shoes for later
#
# find a new way to define where the player begins in the map 
# (different from player initial rectangle bc always in the center)
# can't just have one per level bc multiple entrances / exits
# 
# interaction with environment
# textboxes
# npc movement
#
# 
#
# when update graphics ? work with someone to do it ? 
#
# 








pygame.init()



screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

player = pygame.Rect((settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2,
                               settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2,
                               settings.GRID_SIZE, settings.GRID_SIZE))
player_x = settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2
player_y = settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2


clock = pygame.time.Clock()

facing = settings.FACING.RIGHT

def draw_map(map):
    offsetx = player_x - (settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2)
    offsety = player_y - (settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2)
    for row_index, row in enumerate(map):
        for col_index, col in enumerate(row):
            x = col_index * settings.GRID_SIZE
            y = row_index * settings.GRID_SIZE
            #these are going to be the definitions of sprite types, should also add attributes for places you can move to new maps and stuff
            if col == 'x':
                pygame.draw.rect(screen, (0, 0, 0), (x - offsetx, y - offsety, settings.GRID_SIZE, settings.GRID_SIZE))
            elif col == 'g':
                pygame.draw.rect(screen, (39, 98, 94), (x - offsetx, y - offsety, settings.GRID_SIZE, settings.GRID_SIZE))
            elif col == 'b':
                pygame.draw.rect(screen, (39, 98, 155), (x - offsetx, y - offsety, settings.GRID_SIZE, settings.GRID_SIZE))
            #examples of how i imagine this working eventually
            #elif col == 'm':
            #   draw_sprite(x - offsetx, y - offsety, "left_mountain")
            #elif col == 'oak':
            #   draw_sprite(x - offsetx, y - offsety, "prof_oak")


#checks to see if the player can move where it wants to go
def check_direction(direction, map):
    if (direction == settings.FACING.LEFT):
        if (map[(int)(player_y // settings.GRID_SIZE)][(int)((player_x // settings.GRID_SIZE) - 1)] == 'x'):
            return False
        else: return True
    elif (direction == settings.FACING.RIGHT):
        if (map[(int)(player_y // settings.GRID_SIZE)][(int)((player_x // settings.GRID_SIZE) + 1)] == 'x'):
            return False
        else: return True
    elif (direction == settings.FACING.UP):
        if (map[(int)((player_y // settings.GRID_SIZE) - 1)][(int)(player_x // settings.GRID_SIZE)] == 'x'):
            return False
        else: return True
    elif (direction == settings.FACING.DOWN):
        if (map[(int)((player_y // settings.GRID_SIZE) + 1)][(int)(player_x // settings.GRID_SIZE)] == 'x'):
            return False
        else: return True


run = True


while run:
    map = maps.TEST_MAP
    draw_map(map)

    pygame.draw.rect(screen, (255, 0, 0), player)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    #makes a marker to show the direction the character is facing
    if facing == settings.FACING.LEFT:
        pygame.draw.rect(screen, (255, 255, 255), (player.left, player.top, 2, settings.GRID_SIZE))
    elif facing == settings.FACING.RIGHT:
        pygame.draw.rect(screen, (255, 255, 255), (player.right - 2, player.top, 2, settings.GRID_SIZE))
    elif facing == settings.FACING.UP:
        pygame.draw.rect(screen, (255, 255, 255), (player.left, player.top, settings.GRID_SIZE, 2))
    elif facing == settings.FACING.DOWN:
        pygame.draw.rect(screen, (255, 255, 255), (player.left, player.bottom - 2, settings.GRID_SIZE, 2))

    # Adjust the player's position based on the keys held
    if keys[pygame.K_a]:  # Ensure the player stays within the screen
        if facing == settings.FACING.LEFT and check_direction(settings.FACING.LEFT, map):
            player_x -= settings.GRID_SIZE            
        facing = settings.FACING.LEFT
    elif keys[pygame.K_d]:  # Ensure the player stays within the screen
        if facing == settings.FACING.RIGHT and check_direction(settings.FACING.RIGHT, map):
            player_x += settings.GRID_SIZE  # Move right by one grid unit
        facing = settings.FACING.RIGHT
    elif keys[pygame.K_w]:  # Ensure the player stays within the screen
        if facing == settings.FACING.UP and check_direction(settings.FACING.UP, map):
            player_y -= settings.GRID_SIZE  # Move up by one grid unit
        facing = settings.FACING.UP
    elif keys[pygame.K_s]:  # Ensure the player stays within the screen
        if facing == settings.FACING.DOWN and check_direction(settings.FACING.DOWN, map):
            player_y += settings.GRID_SIZE  # Move down by one grid unit
        facing = settings.FACING.DOWN

    pygame.display.update()
    clock.tick(settings.FPS)

pygame.quit()
