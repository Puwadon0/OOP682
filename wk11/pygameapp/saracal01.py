import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()

full_sheet = pygame.image.load("sara/sara-cal1.png")

w = full_sheet.get_width() // 3
h = full_sheet.get_height() // 2

sara = full_sheet.subsurface(pygame.Rect(0, 0, w, h))

font = pygame.font.SysFont("prompt", 36)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    
    text = font.render(f"{clock.get_fps():.0f}", True, (0, 0, 0))
    screen.blit(text, (300, 230))
    screen.blit(sara, (50, 50))

    pygame.display.update()
    clock.tick(90)

pygame.quit()