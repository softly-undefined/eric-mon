import pygame
import settings
import maps
from tile import Tile
from maps import Map
import math

#Eric Bennett, 2/20/24
#
# things left to do:
#
#
# Get off the tick based system of movement !!! Alphas and fancy shi
# basically make it a greater>= expected location to check for grid placement and snap back
# will also allow for sprinting halfway through a block
#
# npc movement (should be done under the tile class?)
# 
# THEN haven't even started on the battle screen, everything going along with that
# creating a more enjoyable game loop
# going to include pokemon? how should fighting with enemies work?
# the interaction of a battle mechanic with the current interact mechanics is interesting
# maybe go with different enemies ? i wanna do some sort of twist on the regular pkmn
#
# Things I like/would like to keep about the pokemon game loop:
# * Levelling system
# * Probably want turn-based ?
# * some sort of random encounter to make it seem like more of an alive world.
#
#
#
# when update graphics ? work with someone to do it ? 
# make the interaction text show up on the screen itself, 
# also make it go through more than one output for long text
# did a bit of this sprite stuff! also a bit of map stuff its super interesting
#






pygame.init()
screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))

pygame.display.set_caption('eric-mon')

#defines first map placement



player_pos = [3*settings.GRID_SIZE, 3*settings.GRID_SIZE]
#need the two values because its passing the variable by referene
#player pos is relative to the map, player will still always be in the center of the screen

clock = pygame.time.Clock()

#starts facing right, this variable will continually be updated
facing = settings.FACING.RIGHT


#uploads the pron sprite sheet 
player_sheet = pygame.image.load('pron_sheet.png')
#uploads the test map
map_sheet = pygame.transform.scale(pygame.image.load('map_sheet.png'), (settings.GRID_SIZE * 15, settings.GRID_SIZE * 15))


# defines the four states of the pron sprite to be used in draw_pron
# reads the sheet and scales to grid size
player_images = {
    settings.FACING.LEFT: pygame.transform.scale(player_sheet.subsurface(pygame.Rect(10, 10, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE)),
    settings.FACING.RIGHT: pygame.transform.scale(player_sheet.subsurface(pygame.Rect(0, 10, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE)),
    settings.FACING.UP: pygame.transform.scale(player_sheet.subsurface(pygame.Rect(10, 0, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE)),
    settings.FACING.DOWN: pygame.transform.scale(player_sheet.subsurface(pygame.Rect(0, 0, 10, 10)), (settings.GRID_SIZE, settings.GRID_SIZE))
}




def get_position():
    return player_pos[0], player_pos[1]

def get_cell_position():
    return  math.floor(player_pos[1]), math.floor(player_pos[0])


#draws pron facing the direction of facing
def draw_pron():
    screen.blit(player_images[facing], settings.SCREEN_CENTER)

#draws the map! inside this function sprite stuff will be done !
def draw_map():
    global active_map 
    pos_x, pos_y = get_position()

    offsetx = pos_x - (settings.SCREEN_WIDTH // 2 - settings.GRID_SIZE // 2)
    offsety = pos_y - (settings.SCREEN_HEIGHT // 2 - settings.GRID_SIZE // 2)
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

    if active_map.name == "TESTING_ZONE":
        screen.blit(map_sheet, [x - offsetx - (11 * settings.GRID_SIZE), y - offsety - (12 * settings.GRID_SIZE)])



# checks if player can move to the location its facing in and wants to move in
# 
def check_direction():
    global active_map 
    #where code to switch maps is
    cell_pos_x, cell_pos_y = get_cell_position()
    
    facing_tile = active_map.grid[(cell_pos_x // settings.GRID_SIZE) + facing.value[1]][((cell_pos_y // settings.GRID_SIZE) + facing.value[0])]
    #print(f"facing: {(cell_pos_x // settings.GRID_SIZE) + facing.value[1]}, {((cell_pos_y // settings.GRID_SIZE) + facing.value[0])}")
    #print(f" player x {player_pos[0]} player y {player_pos[1]}")
    #print(f" ground? {facing_tile.is_ground}")
    if facing_tile.is_door:
        print("ABOUT TO TELEPORT")
        player_pos[0] = facing_tile.door_coords[0] * settings.GRID_SIZE
        player_pos[1] = facing_tile.door_coords[1] * settings.GRID_SIZE
        screen.fill((0,0,0)) #maybe do this another way in the future, clears screen

        active_map = maps.read_map(facing_tile.door_map) #FIX HERE ?
        
        
        print("TELEPORT BWOOoSH")
        return False

    
    return facing_tile.is_ground

#maybe in the future use target position
#tween: given alpha moving to x
def move_one(is_moving): 
    #cell_pos_y, cell_pos_x = get_cell_position()
    if is_moving:
        
        player_pos[0] += facing.value[0] * movement_speed.value # multiply this by movement speed eventually
        player_pos[1] += facing.value[1] * movement_speed.value # 
        draw_map()
        draw_pron()
    
    
    if player_pos[0] % settings.GRID_SIZE == 0 and player_pos[1] % settings.GRID_SIZE == 0:
        #runs every time that you hit a grid line
        return False
    

    return True
    #    player_pos[0] += facing.value[0]
    #    player_pos[1] += facing.value[1]
    #    draw_map()
    #    draw_pron()

def display_message(text):
    can_move = False
    for i in range(100000):
        print(f"{i} cum")
    can_move = True



run = True
active_map = maps.read_map("UP_TOWN")
test = 1
num_ticks = 0
last_time = pygame.time.get_ticks()
movement = settings.MOVEMENT.WALK
can_move = True

time_down=0

# --------------------------------THE RUN LOOP!!!----------------------------------------
draw_map()
draw_pron()

move = False
is_moving = False

while run:
    
    draw_map()
    draw_pron()

    pygame.display.set_caption(f"{(player_pos[1] // settings.GRID_SIZE)},{(player_pos[0] // settings.GRID_SIZE)}") #mostly for debugging rn

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() # Get the keys pressed

    #checks for interactions
    
    if keys[pygame.K_i]: #equivalent for clicking a on the gameboy
        cell_pos_y, cell_pos_x = get_cell_position()
        if active_map.grid[(cell_pos_y // settings.GRID_SIZE) + facing.value[1]][(cell_pos_x // settings.GRID_SIZE) + facing.value[0]].is_interactable:
            display_message(active_map.grid[(cell_pos_y // settings.GRID_SIZE) + facing.value[1]][(cell_pos_x // settings.GRID_SIZE) + facing.value[0]].interact_text)

    if keys[pygame.K_j]:
        movement = settings.MOVEMENT.RUN
    elif keys[pygame.K_p]:
        movement = settings.MOVEMENT.BIKE
    else:
        movement = settings.MOVEMENT.WALK



    #alpha time stuff goes here
    #curr_time = pygame.time.get_ticks()


    #elapsed_time = last_time - curr_time
    #last_time = curr_time

    #move_distance = (elapsed_time * 1000)/settings.MOVEMENT_SPEED
    #move_distance *= settings.GRID_SIZE

    #move_distance = 1


    
    # MOVEMENT COMMANDS
    # also makes it so when changing direction it takes an extra press of the key so you can turn without moving
    if can_move:


        if not is_moving: # if not moving
            
            direction_check = check_direction()
            if movement == settings.MOVEMENT.WALK:
                movement_speed = settings.MOVEMENT.WALK
            elif movement == settings.MOVEMENT.RUN:
                movement_speed = settings.MOVEMENT.RUN
            else:
                movement_speed = settings.MOVEMENT.BIKE

            
            #print(f"direction check {direction_check}")
            if keys[pygame.K_a]:  # Ensure the player stays within the screen 
                if facing == settings.FACING.LEFT and direction_check:
                    is_moving = True               
                facing = settings.FACING.LEFT
            elif keys[pygame.K_d]:  # Ensure the player stays within the screen
                if facing == settings.FACING.RIGHT and direction_check:
                    is_moving = True 
                facing = settings.FACING.RIGHT
            elif keys[pygame.K_s]:  # Ensure the player stays within the screen
                if facing == settings.FACING.DOWN and direction_check:
                    is_moving = True 
                facing = settings.FACING.DOWN
            elif keys[pygame.K_w]:  # Ensure the player stays within the screen
                if facing == settings.FACING.UP and direction_check:
                    is_moving = True 
                facing = settings.FACING.UP
        
        is_moving = move_one(is_moving)
        print(is_moving)
    
        
    
    num_ticks += 1
    pygame.display.update()
    clock.tick(settings.FPS)
    

pygame.quit()
