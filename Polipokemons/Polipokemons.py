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
    if (gameState.mode == 'map'):
        screen.fill((0,0,0))
        map.draw_map(screen)
        gui.draw_gui_map()
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
        screen.fill((0,255,0))
        if gameState.battleType == 'boss':            
            gui.draw_gui_battle()
            boss.speak(screen, gui)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameState.done = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    boss.speakCounterIncrement()

            gui.proceed_input(event)

        
    pygame.display.flip()

