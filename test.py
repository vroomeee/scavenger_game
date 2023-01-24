import pygame

win = pygame.display.set_mode((500, 500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    pygame.draw.rect(win, (40, 40, 200), pygame.Rect(23, 344, 40, 40))
    print(pygame.Rect(23, 344, 40, 40).centerx)
    pygame.display.update()