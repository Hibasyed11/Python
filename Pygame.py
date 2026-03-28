import pygame
pygame.init()
display_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Adding image + background image.')
background_image = pygame.image.load('background.png').convert()
background_image = pygame.transform.scale(background_image, (500, 500))
penguin_image = pygame.image.load('hello penguin.png').convert_alpha()
penguin_image = pygame.transform.scale(penguin_image, (200, 200))
penguin_image.set_colorkey((255, 255, 255))
penguin_rect = penguin_image.get_rect(center=(250, 220))
text=pygame.font.Font(None, 36).render('Hello World!', True, pygame.Color('black'))
text_rect=text.get_rect(center=(500//2, 500//2+110))
def  game_loop():
    clock=pygame.time.Clock()
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        display_surface.blit(background_image, (0, 0))
        display_surface.blit(penguin_image, penguin_rect)
        display_surface.blit(text, text_rect)
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
if __name__=='__main__':
    game_loop()