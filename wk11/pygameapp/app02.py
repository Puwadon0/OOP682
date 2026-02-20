import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    clock.tick(60)
    screen.fill((255, 255, 255))
    font = pygame.font.SysFont("prompt", 36)
    text = font.render(f"{clock.get_fps():.0f}", True, (0, 0, 0))
    screen.blit(text, (300, 230))
    pygame.display.update()


pygame.quit()
