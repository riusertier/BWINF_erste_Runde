import pygame
import random

anzahl_keime = 5


raster_breite = 900
raster_höhe = 500


WIN = pygame.display.set_mode((raster_breite, raster_höhe))
pygame.display.set_caption("Verzinkt")

WHITE = (255,255,255)
FPS = 30

def draw_window():
    WIN.fill(WHITE)
    pygame.draw.line(WIN, (0,0,0), (130, 100), (130, 100)) # pixel
    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
        

    pygame.quit()

if __name__ == "__main__":
    main()