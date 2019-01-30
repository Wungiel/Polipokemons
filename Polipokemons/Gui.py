import pygame, thorpy


def change_state_loop(gui):
    gui.gameState.changeState()

class GUI(object):

    black = pygame.Color(0,0,0)
    brown = pygame.Color(244,164,96)

    def __init__(self, gameState, screen):

        self.gameState = gameState        
        self.font = pygame.font.SysFont("monospace", 15)
        self.screen = screen

        pokemon_button = thorpy.make_button("Pokemons", func=change_state_loop, params = {"gui":self} )
        quit_button = thorpy.make_button("Quit", func=change_state_loop, params = {"gui":self})
        self.boxMap = thorpy.Box.make(elements=[pokemon_button,quit_button])
        self.menuMap = thorpy.Menu(self.boxMap)
        for element in self.menuMap.get_population():
            element.surface = screen
        self.boxMap.set_topleft((0,502))

        attack_button = thorpy.make_button("Attack", func=change_state_loop, params = {"gui":self} )
        escape_button = thorpy.make_button("Escape", func=change_state_loop, params = {"gui":self})
        self.boxBattle = thorpy.Box.make(elements=[attack_button,escape_button])
        self.menuBattle = thorpy.Menu(self.boxBattle)
        for element in self.menuBattle.get_population():
            element.surface = screen
        self.boxBattle.set_topleft((0,502))
        pass


    def draw_gui_map(self):
        pygame.draw.rect(self.screen, GUI.brown , pygame.Rect(0, 498, 800, 4))
        pygame.draw.rect(self.screen, GUI.black , pygame.Rect(0, 502, 800, 98))
        
        self.boxMap.blit()
        self.boxMap.update()
        return

    def draw_gui_battle(self):
        pygame.draw.rect(self.screen, GUI.brown , pygame.Rect(0, 498, 800, 4))
        pygame.draw.rect(self.screen, GUI.black , pygame.Rect(0, 502, 800, 98))

        self.boxBattle.blit()
        self.boxBattle.update()      
        return

    def show_text(self, text):
        rectangle = pygame.draw.rect(self.screen,(255,255,255),pygame.Rect(200,280,350,100))
        text = self.font.render(text,1,(0,0,0))
        self.screen.blit(text, rectangle)


    def proceed_input(self, event):
        if(self.gameState == 'map'):
            self.menuMap.react(event)
        else:
            self.menuBattle.react(event)
