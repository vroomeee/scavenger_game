# this is a game about surviving in a fallen world
import pygame
import sys
import math
import handle_x
from random import randint
import time

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

win_size = (800, 600)

# renders = pygame.Surface(render_screen_size)
# actual display

log_image = pygame.image.load("logs.png")

game_running = True
list_of_logs = []
tile_size = 30
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

class spawn_en:
    def __init__(self):
        self.st = time.time()
        self.enemy_size = 30
        self.enemies = []
        self.enemyd = 50
        self.speed = 0.3
    def spawn(self):
        if time.time() - self.st > 1/wave_num * 3:
            self.st = time.time()
            self.SpawnEnemy()
            list_of_logs.append(log(pygame.mouse.get_pos()[0] / 1.5, pygame.mouse.get_pos()[1] / 1.5, randint(40, 60)))
    def SpawnEnemy(self):
        while True:
            randomx = randint(0, win_size[0])
            if player1.x - self.enemyd < randomx < player1.x + self.enemyd:
                pass
            else:
                if 0 < randomx < win_size[1] - self.enemy_size:
                    break
        while True:
            randomy = randint(0, win_size[1])
            if player1.y - self.enemyd < randomy < player1.y + self.enemyd:
                pass
            else:
                if 0 < randomy < win_size[1] - self.enemy_size:
                    break
        self.enemies.append((randomx, randomy))
    def DrawEnemy(self):
        for instance_enemy in self.enemies:
            pygame.draw.rect(win, pygame.Color("red"), pygame.Rect(instance_enemy[0], instance_enemy[1], self.enemy_size, self.enemy_size))
    def EnemyFollow(self):
        for instance in self.enemies:
            settled_x = False
            settled_y = False
            dx = abs(player1.centerx - instance[0] - self.enemy_size/2)
            dy = abs(player1.centery - instance[1] - self.enemy_size/2)
            if dx < self.speed:
                instance[0] = player1.centerx
                break
                #CURRENTLY WORKING HERE






wave_num = 1
wave_times = [0, 10, 30, 60]
ENEMYSYS = spawn_en()
def waves():
    global wave_num
    ct = time.time()
    for i in range(0, len(wave_times) - 1):
        if wave_times[i] < ct < wave_times[i+1]:
            wave_num = i + 1
            break
    ENEMYSYS.spawn()
    ENEMYSYS.DrawEnemy()


collision_list = []

class player:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.size = [size, size]
        self.speed = 0.5
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])
        self.settled_x = False
        self.log = 0

    def updateRect(self):
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def draw(self):
        pygame.draw.rect(win, (174, 198, 207), self.rect, 0, 7)

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
        # text_mid(text([self.vx, self.vy], get_font(100)), 150)
        if not self.vx == 0 or not self.vy == 0:
            self.tile_collision(tiles)
    def reset(self):
        self.x = 200
        self.y = 200
        self.updateRect()

    def tile_collision(self, tiles):
        collision_list = ENEMYSYS.enemies + tiles
        handle_x.handle_x(self, collision_list, tile_size, win_size)


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
    def add(self):
        list_of_logs.append(self)


def check_logs():
    global list_of_logs
    for instance in list_of_logs:
        distance = ((player1.rect.centerx - instance.rect.centerx) ** 2 + (
                    player1.rect.centery - instance.rect.centery) ** 2) ** (1 / 2)
        if distance <= player1.size[0] / 2 + instance.size / 2 - 10:
            list_of_logs.remove(instance)
            player1.log += 1


class tile_objects:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = tile_size


def draw_tiles():
    mp = (pygame.mouse.get_pos()[0] / 1.5, pygame.mouse.get_pos()[1] / 1.5)
    if mouse_down and 0 < mp[0] < win_size[0] and 0 < mp[1] < win_size[1]:
        mp_loc = (math.floor(mp[0] / tile_size), math.floor(mp[1] / tile_size))
        tile_coords = [mp_loc[0] * tile_size, mp_loc[1] * tile_size, key_down]
        # rect = pygame.Rect(mp_loc[0] * tile_size, mp_loc[1] * tile_size, tile_size, tile_size)
        if not pygame.Rect.colliderect(player1.rect, pygame.Rect(tile_coords[0], tile_coords[1], tile_size, tile_size))and 0 < mp[0] < win_size[0] and 0 < mp[1] < win_size[1]:
            if key_down == 1:
                if not tile_coords in tile_list:
                    tile_list.append(tile_coords)
            if key_down == 2:
                tile_coords[2] = 1
                if tile_coords in tile_list:
                    tile_list.remove(tile_coords)
    for tile in tile_list:
        pygame.draw.rect(win, pygame.Color(155, 103, 60), pygame.Rect(tile[0], tile[1], tile_size, tile_size))



player1 = player(200, 200, 30)
log1 = log(300, 300, 50)
log1.add()



# game
def main(dt):
    player1.movement(dt, tile_list)
    player1.draw()
    draw_tiles()
    draw_logs()
    check_logs()
    waves()

# basic game loop
while True:
    import start
    win = pygame.Surface(win_size)
    render = pygame.display.set_mode((1200, 900))
    pygame.display.set_caption("Scavenger")
    player1.x = 200
    player1.y = 200
    st = time.time()
    while game_running:
        dt = clock.tick(480)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if key_down == 3:
                    list_of_logs.append(log(pygame.mouse.get_pos()[0] / 1.5, pygame.mouse.get_pos()[1] / 1.5, randint(40, 60)))
                mouse_down = True
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key_down = 1
                if event.key == pygame.K_2:
                    key_down = 2
                if event.key == pygame.K_3:
                    key_down = 3
                if event.key == pygame.K_r:
                    player1.reset()
                    tile_list.clear()
                    ENEMYSYS.enemies.clear()
        win.fill((153, 147, 178))
        main(dt)
        render.blit(pygame.transform.scale(win, (1200, 900)), (0, 0))
        # render.blit(win, (player1.x, player1.y))
        pygame.display.update()
