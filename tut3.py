import pygame
pygame.init()

# Creating Window
gameWindow=pygame.display.set_mode((1200,500))
pygame.display.set_caption("My First Game")

# Game Specific Variable
exit_game=False
game_over=False

# Creating A Game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
    
pygame.quit()
quit()
