# This module was made on the basis that there aren't any slim tiles(blocks) such as walls.
# To implement slim walls, edit the x value into nearly half
import pygame, math

x = None
y = None
vector = 1


def handle_x(self, real_tiles, tile_size):
    global vector, x, y
    self.settled_x = False
    for tile in real_tiles:
        if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
            self.rect.x += self.vx
            self.rect.y += self.vy
            return
    self.rect.x += self.vx
    for tile in real_tiles:
        if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
            if self.vx > 0:
                self.rect.x = tile[0] - self.rect.w
            if self.vx < 0:
                self.rect.x = tile[0] + tile_size
            break
    self.x = self.rect.x
    self.rect.y += self.vy
    for tile in real_tiles:
        if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
            if self.vy > 0:
                self.rect.y = tile[1] - self.rect.h
            if self.vy < 0:
                self.rect.y = tile[1] + tile_size
            break
    self.y = self.rect.y
    #     self.on_floor = False
    #     former_x = self.rect.x

    # for tile in real_tiles:
    #     if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
    #         return None
    #
    # if self.vx > 0:
    #     vector = 1
    # elif self.vx < 0:
    #     vector = -1
    # else:
    #     print("error: player vx is 0 but got passed onto handle_x.py")
    #
    # x = self.size[0] + tile_size - 1
    # y = math.floor(self.vx / x)
    #
    # print(y)
    # for i in range(1, vector * y + 1):
    #     self.rect.x += x
    #     for tile in real_tiles:
    #         if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
    #             self.rect.x = tile.x - self.w
    #             return None
    #
    # self.rect.x += self.vx - x * y


