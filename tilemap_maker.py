import pygame, sys, math, pyperclip

tile_num = 0
tile_size = 16 #16
screen_w = 600
screen_h = 400

WIN = pygame.display.set_mode((screen_w, screen_h))



var = screen_w//tile_size
var2 = screen_h//tile_size
print(var, var2)

mouse_down = False


color_tiles = []

for i in range(0, math.ceil(var2) + 1):
    xtiles = []
    for n in range(0, math.ceil(var) + 1):
        xtiles.append("0")         #pygame.Rect(i*tile_size, n*tile_size, tile_size, tile_size)
    color_tiles.append(xtiles)




dirt_img = pygame.image.load("dirt.png")
dirt_img = pygame.transform.scale(dirt_img, (tile_size, tile_size))

grass_img = pygame.image.load("grass.png")
grass_img = pygame.transform.scale(grass_img, (tile_size, tile_size))
mouse_down = False


def draw_tiles():
    global mouse_down, tile_num
    WIN.fill((230, 156, 92))

    for i in range(0, var2+1):
        for n in range(0, var+1):
            if color_tiles[i][n] == "1":
                WIN.blit(dirt_img, (n*tile_size, i*tile_size))
            if color_tiles[i][n] == "2":
                WIN.blit(grass_img, (n*tile_size, i*tile_size))

    mp = pygame.mouse.get_pos()
    mp_loc = (math.floor(mp[0]/tile_size), math.floor(mp[1]/tile_size))

    for y in range(0, var2 + 1):
        for x in range(0, var + 1):
            pygame.draw.rect(WIN, (245,245,220), pygame.Rect(x*tile_size, y*tile_size, tile_size, tile_size), 1)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            print(color_tiles)
            pyperclip.copy(str(color_tiles))
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_down = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_down = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                tile_num = 0
                
            if event.key == pygame.K_1:
                tile_num = 1
        
            if event.key == pygame.K_2:
                tile_num = 2

            if event.key == pygame.K_3:
                tile_num = 3

            if event.key == pygame.K_4:
                tile_num = 4
    # print(color_tiles[0][50])
    if mouse_down and mp[0] > 0 and mp[0] < screen_w and mp[1] > 0 and mp[1] < screen_h:
        color_tiles[mp_loc[1]][mp_loc[0]] = str(tile_num)
    


while True:
    draw_tiles()

    pygame.display.update()