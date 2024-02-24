import pygame
import settings
import maps
from tile import Tile
from maps import Map


#Eric Bennett, 2/20/24
#
# things left to do:
#
# slow the player down!! need to have running shoes for later
# Idk why this is just the end of me ^^
#
# npc movement
# 
# THEN haven't even started on the battle screen, everything going along with that
# creating a more enjoyable game loop
# going to include pokemon? how should fighting with enemies work?
#
# when update graphics ? work with someone to do it ? 
# make the interaction text show up on the screen itself, 
# also make it go through more than one output for long text
# did a bit of this sprite stuff! 
#

pygame.init()



screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption('eric-mon')

#defines first map placement



#draws player at center of screen and defines the place on the map using player_pos[0] player_pos[1]
#player = pygame.Rect((settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2,
#                               settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2,
#                               settings.GRID_SIZE, settings.GRID_SIZE))

SCREEN_CENTER = [settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2, settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2]
player_pos = [settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2, settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2]


clock = pygame.time.Clock()

#starts facing right
facing = settings.FACING.RIGHT


#uploads the pron sprite sheet 
player_sheet = pygame.image.load('pron_sheet.png')

player_images = {
    "left": pygame.transform.scale(player_sheet.subsurface(pygame.Rect(10, 10, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE)), #reads the shit and scales to grid size
    "right": pygame.transform.scale(player_sheet.subsurface(pygame.Rect(0, 10, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE)),
    "up": pygame.transform.scale(player_sheet.subsurface(pygame.Rect(10, 0, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE)),
    "down": pygame.transform.scale(player_sheet.subsurface(pygame.Rect(0, 0, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE))
}


def draw_pron():
    #player position in the playerpos variable
    if facing == settings.FACING.LEFT:
        screen.blit(player_images["left"], SCREEN_CENTER)
    elif facing == settings.FACING.RIGHT:
        screen.blit(player_images["right"], SCREEN_CENTER)
    elif facing == settings.FACING.UP:
        screen.blit(player_images["up"], SCREEN_CENTER)
    elif facing == settings.FACING.DOWN:
        screen.blit(player_images["down"], SCREEN_CENTER)

draw_pron()

#draws the map! inside this function sprite stuff will be done !
def draw_map():
    global active_map 
    offsetx = player_pos[0] - (settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2)
    offsety = player_pos[1] - (settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2)
    for row_index, row in enumerate(active_map.grid):
        for col_index, col in enumerate(row):
            x = col_index * settings.GRID_SIZE
            y = row_index * settings.GRID_SIZE
            # these are going to be the definitions of sprite types, should also add attributes for places you can move to new maps and stuff
            # attribute is_sprite created but not used right now, use it for 
            # when sprite actually needs drawing (ground and everything will be in background)
            if col.is_ground == False:
                if col.is_interactable:
                    pygame.draw.rect(screen, (170, 0, 0), (x - offsetx, y - offsety, settings.GRID_SIZE, settings.GRID_SIZE))
                else:
                    pygame.draw.rect(screen, (0, 0, 0), (x - offsetx, y - offsety, settings.GRID_SIZE, settings.GRID_SIZE))
            else:
                if col.is_door == True:
                    pygame.draw.rect(screen, (0, 0, 170), (x - offsetx, y - offsety, settings.GRID_SIZE, settings.GRID_SIZE))
                else:
                    pygame.draw.rect(screen, (75, 75, 175), (x - offsetx, y - offsety, settings.GRID_SIZE, settings.GRID_SIZE))




# checks if player can move to the location its facing in and wants to move in
# 
def check_direction():
    global active_map 
    #where code to switch maps is
    facing_tile = active_map.grid[(player_pos[1] // settings.GRID_SIZE) + facing.value[1]][((player_pos[0] // settings.GRID_SIZE) + facing.value[0])]
    if facing_tile.is_door:
        player_pos[0] = facing_tile.door_coords[0] * settings.GRID_SIZE
        player_pos[1] = facing_tile.door_coords[1] * settings.GRID_SIZE
        screen.fill((0,0,0)) #maybe do this another way in the future, clears screen

        active_map = maps.read_map(facing_tile.door_map) #FIX HERE
        test = 2
        print(test)
        print(active_map.grid[0][0].is_ground) #its 
        
        print("TELEPORT BWOOoSH")
        return False


    return facing_tile.is_ground





run = True
active_map = maps.read_map("TEST_MAP")
test = 1

while run:
    draw_map()
    

    draw_pron()
    pygame.display.set_caption(f"{(player_pos[1] // settings.GRID_SIZE)},{(player_pos[0] // settings.GRID_SIZE)}")

    #draw_facing()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get the keys pressed
    keys = pygame.key.get_pressed()

    


    #checks for interactions
    if keys[pygame.K_i]: #equivalent for clicking a on the gameboy
        
        active_map.grid[(player_pos[1] // settings.GRID_SIZE) + facing.value[1]][(player_pos[0] // settings.GRID_SIZE) + facing.value[0]].interact()
        
        
        

    elif keys[pygame.K_j]: #should eventually allow for sprint and stuff like that?
        print("ooga booga")

    # MOVEMENT COMMANDS
    # also makes it so when changing direction it takes an extra press of the key so you can turn without moving
    if keys[pygame.K_a]:  # Ensure the player stays within the screen
        if facing == settings.FACING.LEFT and check_direction():
            player_pos[0] -= settings.GRID_SIZE          
        facing = settings.FACING.LEFT
    elif keys[pygame.K_d]:  # Ensure the player stays within the screen
        if facing == settings.FACING.RIGHT and check_direction():
            player_pos[0] += settings.GRID_SIZE  # Move right by one grid unit
        facing = settings.FACING.RIGHT
    elif keys[pygame.K_w]:  # Ensure the player stays within the screen
        if facing == settings.FACING.UP and check_direction():
            player_pos[1] -= settings.GRID_SIZE  # Move up by one grid unit
        facing = settings.FACING.UP
    elif keys[pygame.K_s]:  # Ensure the player stays within the screen
        if facing == settings.FACING.DOWN and check_direction():
            player_pos[1] += settings.GRID_SIZE  # Move down by one grid unit
        facing = settings.FACING.DOWN

    pygame.display.update()
    clock.tick(settings.FPS)

pygame.quit()
