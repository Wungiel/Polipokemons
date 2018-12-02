import pygame, thorpy
from map import Map
from gui import GUI


#Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))


#Data setup
map = Map('map.png', 'tiles.png')
gui = Gui()
map.generate_map()
done = False
TILE_SIZE = 40
position = [0,0]

#Main loop
while not done:
    map.draw_map(screen, position)
    gui.draw_gui(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_a:
                position[0]-=1
            elif event.key==pygame.K_d:
                position[0]+=1
            elif event.key==pygame.K_w:
                position[1]-=1
            elif event.key==pygame.K_s:
                position[1]+=1
        
    pygame.display.flip()

