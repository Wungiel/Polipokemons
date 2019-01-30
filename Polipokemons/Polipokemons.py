import pygame, thorpy
from map import Map
from gui import GUI
from gameState import GameState
from player import Player
from boss import Boss

def set_done():
    done = False

#Initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
myfont = pygame.font.SysFont("monospace", 15)

#Data setup
map = Map('map.png', 'tiles.png')
gameState = GameState()
gui = GUI(gameState, screen)
player = Player('player.png')
boss = Boss('boss.png')
#pokemons = Pokemon()
map.generate_map()
TILE_SIZE = 40
position = [0,0]

#Main loop
while not gameState.done:
    screen.fill((0,0,0))
    if (gameState.mode == 'map'):
        map.draw_map(screen)
        gui.draw_gui(screen)
        player.draw_player(screen)
        boss.draw_boss(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState.done = True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a:
                    movement = (-1,0)
                elif event.key==pygame.K_d:
                    movement =(1,0)
                elif event.key==pygame.K_w:
                    movement = (0,-1)
                elif event.key==pygame.K_s:
                    movement = (0,1)
                else:
                    movement = (0,0)

                if (boss.check_movement(movement,player.position)):
                    if (map.check_movement(movement,player.position)): 
                        player.move_player(movement)
                else:
                    gameState.changeMode()
            gui.proceed_input(event)
 
    else:
        pygame.draw.rect(screen, (90,90,90), (0,400,100,100))
        label = myfont.render("Some text!", 1, (255,255,255))
        screen.blit(label, (100, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameState.done = True

        
    pygame.display.flip()

