import pygame

pygame.init()

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Dance Game')
clock = pygame.time.Clock()


def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                close_game()
        # TODO: Create game intro


def main():
    pygame.quit()
    quit()


# this calls the 'main' function when this script is executed
if __name__ == '__main__':
    main()
