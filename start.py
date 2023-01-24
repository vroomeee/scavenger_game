import pygame
#this is a game about surviving in a fallen world
import pygame, sys

pygame.init()
pygame.font.init()

win_size = (800, 600)
win = pygame.display.set_mode(win_size)
render = pygame.Surface(win_size)
pygame.display.set_caption("Scavenger")
# renders = pygame.Surface(render_screen_size)

def get_font(size):
    font = pygame.font.SysFont('comicsans', size)
    return font

def text(text, font):
    main_text = font.render(str(text), 1, pygame.Color("black"))
    return main_text

def text_mid(main_text, y):
    win.blit(main_text, (win_size[0] / 2 - main_text.get_width() / 2, y))

game_running = True
while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            game_running = False
    win.fill((153, 147, 178))
    text_mid(text("Scavenger", get_font(100)), 150)
    text_mid(text("press any key to start", get_font(30)), 350)
    pygame.display.update()