import pygame
pygame.init()

# Creating Window
screen_width= 800
screen_height= 600
gameWindow=pygame.display.set_mode((screen_width,screen_height))

# title of the game
pygame.display.set_caption("My First Game")
pygame.display.update()

# Colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

# Game Specific Variable
exit_game=False
game_over=False
snake_x=100
snake_y=60
snake_size=40

# Creating A Game loop
while not exit_game:
    for event in pygame.event.get():
        print(event)
        if event.type==pygame.QUIT:
            exit_game=True
        # if event.type==pygame.KEYDOWN:
        #     if event.key==pygame.K_RIGHT:
        #         print("You have pressed right arrow key")
    gameWindow.fill(white)
    pygame.draw.rect(gameWindow,red,[snake_x,snake_y,snake_size,snake_size])
    pygame.display.update()

pygame.quit()
quit()
