import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("My first game screen")

background = (58, 58, 58)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background)

    pygame.display.update()
pygame.quit()