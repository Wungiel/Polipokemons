import pygame, thorpy


def change_state_loop(gui):
    gui.gameState.changeState()

class GUI(object):

    black = pygame.Color(0,0,0)
    brown = pygame.Color(244,164,96)

    def __init__(self, gameState, screen):
        self.gameState = gameState
        pokemon_button = thorpy.make_button("Pokemons", func=change_state_loop, params = {"gui":self} )
        quit_button = thorpy.make_button("Quit", func=change_state_loop, params = {"gui":self})
        self.box = thorpy.Box.make(elements=[pokemon_button,quit_button])
        self.menu = thorpy.Menu(self.box)
        for element in self.menu.get_population():
            element.surface = screen
        self.box.set_topleft((0,502))
        pass


    def draw_gui(self, screen):
        pygame.draw.rect(screen, GUI.brown , pygame.Rect(0, 498, 800, 4))
        pygame.draw.rect(screen, GUI.black , pygame.Rect(0, 502, 800, 98))\
        
        self.box.blit()
        self.box.update()
        return

    def proceed_input(self, event):
        self.menu.react(event)


