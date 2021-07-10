import pygame
pygame.init()

# Creating Window
screen_width= 800
screen_height= 600
gameWindow=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("My First Game")
pygame.display.update()

# Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
# Game Specific Variable
exit_game=False
game_over=False

# Creating A Game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.quit:
            exit_game=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_RIGHT:
                print("You have pressed right arrow key")
    gameWindow.fill(white)
    pygame.display.update()

pygame.quit()
quit()
