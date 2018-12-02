import pygame, thorpy
from map import Map
from gui import GUI
from gameState import GameState

def set_done():
    done = False

#Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))


#Data setup
map = Map('map.png', 'tiles.png')
gameState = GameState()
gui = GUI(gameState, screen)
map.generate_map()
TILE_SIZE = 40
position = [0,0]

#Main loop
while not gameState.done:
    screen.fill((0,0,0))
    map.draw_map(screen, position)
    gui.draw_gui(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameState.done = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                position[0]-= 20
            elif event.key==pygame.K_d:
                position[0]+= 20
            elif event.key==pygame.K_w:
                position[1]-= 20
            elif event.key==pygame.K_s:
                position[1]+= 20
        gui.proceed_input(event)
        
    pygame.display.flip()

