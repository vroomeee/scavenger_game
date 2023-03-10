# this is a game about surviving in a fallen world
import pygame
import sys
import math
import handle_x
from random import randint

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

win_size = (800, 600)
win = pygame.display.set_mode(win_size)
render = pygame.Surface(win_size)
pygame.display.set_caption("Scavenger")
# renders = pygame.Surface(render_screen_size)
# actual display

log_image = pygame.image.load("logs.png")

game_running = True
list_of_logs = []
tile_size = 20
tile_list = []
mouse_down = False
key_down = 1


def get_font(size):
    font = pygame.font.SysFont('comicsans', size)
    return font


def text(text, font):
    main_text = font.render(str(text), 1, pygame.Color("black"))
    return main_text


def text_mid(main_text, y):
    win.blit(main_text, (win_size[0] / 2 - main_text.get_width() / 2, y))

class bg:
    def __init__(self):
        pass


class player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = [size, size]
        self.speed = 1
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.settled_x = False

    def updateRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def draw(self):
        pygame.draw.rect(win, (174, 198, 207), self.rect)

    def movement(self, dt, tiles):
        keys = pygame.key.get_pressed()
        self.vx = 0
        self.vy = 0
        if keys[pygame.K_w]:
            self.vy += -self.speed * dt
        if keys[pygame.K_s]:
            self.vy += self.speed * dt
        if keys[pygame.K_a]:
            self.vx += -self.speed * dt
        if keys[pygame.K_d]:
            self.vx += self.speed * dt
        # self.updateRect()
        text_mid(text(self.vx, get_font(100)), 150)
        if not self.vx == 0 or not self.vy == 0:
            self.tile_collision(tiles)


    def tile_collision(self, tiles):
        handle_x.handle_x(self, tiles, tile_size)


def draw_logs():
    for instance in list_of_logs:
        win.blit(instance.image, (instance.x, instance.y))


class log:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.image = pygame.transform.scale(log_image, (self.size, self.size))
        self.rect = pygame.Rect(self.x, self.y, self.size, self.size)
        list_of_logs.append(self)


def check_logs():
    global list_of_logs
    for instance in list_of_logs:
        distance = ((player1.rect.centerx - instance.rect.centerx) ** 2 + (
                    player1.rect.centery - instance.rect.centery) ** 2) ** (1 / 2)
        if distance <= player1.size[0] / 2 + instance.size / 2 - 10:
            list_of_logs.remove(instance)


class tile_objects:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = tile_size


def draw_tiles():
    mp = pygame.mouse.get_pos()
    if mouse_down and 0 < mp[0] < win_size[0] and 0 < mp[1] < win_size[1]:
        mp_loc = (math.floor(mp[0] / tile_size), math.floor(mp[1] / tile_size))
        tile_coords = (mp_loc[0] * tile_size, mp_loc[1] * tile_size, key_down)
        # rect = pygame.Rect(mp_loc[0] * tile_size, mp_loc[1] * tile_size, tile_size, tile_size)
        if not pygame.Rect.colliderect(player1.rect, pygame.Rect(tile_coords[0], tile_coords[1], tile_size, tile_size)):
            if key_down == 1:
                if not tile_coords in tile_list:
                    tile_list.append(tile_coords)
            if key_down == 2:
                if tile_coords in tile_list:
                    tile_list.remove(tile_coords)
    for tile in tile_list:
        pygame.draw.rect(win, pygame.Color('green'), pygame.Rect(tile[0], tile[1], tile_size, tile_size))



player1 = player(200, 200, 50)
log1 = log(300, 300, 50)


# game
def main(dt):
    draw_logs()
    player1.movement(dt, tile_list)
    player1.draw()
    draw_tiles()
    check_logs()


# basic game loop
while True:
    while game_running:
        dt = clock.tick()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if key_down == 3:
                    list_of_logs.append(log(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], randint(40, 60)))
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key_down = 1
                if event.key == pygame.K_2:
                    key_down = 2
                # if event.key == pygame.K_3:
                #     key_down = 3
        win.fill((153, 147, 178))
        main(dt)
        pygame.display.update()
