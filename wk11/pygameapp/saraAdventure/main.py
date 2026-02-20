import sys
import pygame
import chars.sara as hero
pygame.init()


class SaraAdventure(object):
    def __init__(self):
        pygame.init() 
        self.screen = pygame.display.set_mode((400, 300))
        self.clock = pygame.time.Clock()
        self.caption = "Sara the Adventurer"
        self.hero = hero.Hero('sara', 'sara/sara-cal1.png', 50, 50)
        self.font = pygame.font.SysFont("Arial", 48)
        pygame.display.set_caption(self.caption)
        
    def handle_close(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
    def draw_text(self, text, position):
        text_surface = self.font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, position)
                
    def start(self):
        start = pygame.time.get_ticks()
        while True:
            self.handle_close()
            elapsed_time = pygame.time.get_ticks() - start
            self.screen.fill((255, 255, 255))
            self.draw_text("Sara Adventure", (100, 100))
            self.hero.update(self.clock.get_time())
            self.hero.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
        pygame.quit()

if __name__ == "__main__":
    game = SaraAdventure()
    game.start()