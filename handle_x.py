# This module was made on the basis that there aren't any slim tiles(blocks) such as walls.
# To implement slim walls, edit the x value into nearly half
import pygame, math

x = None
y = None
vector = 1


def handle_x(self, real_tiles, tile_size):
    global vector, x, y
    self.settled_x = False
    #     self.on_floor = False
    #     former_x = self.rect.x

    for tile in real_tiles:
        if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
            return None

    if self.vx > 0:
        vector = 1
    elif self.vx < 0:
        vector = -1
    else:
        print("error: player vx is 0 but got passed onto handle_x.py")

    x = self.size[0] + tile_size - 1
    y = math.floor(self.vx / x)

    print(y)
    for i in range(1, vector * y + 1):
        self.rect.x += x
        for tile in real_tiles:
            if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
                self.rect.x = tile.x - self.w
                return None

    self.rect.x += self.vx - x * y

#     if not overlap and self.vx > 0:
#         for i in range(1, math.floor(self.vx/self.size[0]*2) + 1):
#             if not self.settled_x:
#                 self.x += self.size[0]/2
#                 for tile in real_tiles:
#                     if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
#                         self.x = tile[0] - self.size[0]
#                         # self.vx = 0
#                         self.settled_x = True
#                         break
#
# #                     self.on_floor = True
# #                     break
#     if not self.settled_x and self.vx > 0:
#         self.x += self.size[0]/2 * ((self.vx/self.size[0]*2)%1)
#         for tile in real_tiles:
#             if pygame.Rect.colliderect(self.rect, pygame.Rect(tile[0], tile[1], tile_size, tile_size)):
#                 self.x = tile[0] - self.size[0]
#                 # self.vx = 0
#                 self.settled_x = True
#                 break


# what is this shit
# if not self.settled_x and self.vy <= 0:
#     self.rect.y += self.vy
#     # self.settled_x = True
#     self.jumping = True

# self.jumping = False
#                 self.on_floor = True
#                 break

#     if not self.on_floor:
#         self.rect.y = former_y + self.vy
