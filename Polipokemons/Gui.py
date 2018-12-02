import pygame, thorpy

class GUI(object):

    black = pygame.Color(0,0,0)
    brown = pygame.Color(244,164,96)

    def __init__(self):
        pass

    def draw_gui(self, screen):
        pygame.draw.rect(screen, GUI.brown , pygame.Rect(0, 498, 800, 4))
        pygame.draw.rect(screen, GUI.black , pygame.Rect(0, 502, 800, 98))

        pokemon_button = thorpy.make_button("Pokemons", func=thorpy.functions.quit_func)
        quit_button = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
        box = thorpy.Box.make(elements=[pokemon_button,quit_button])
        self.menu = thorpy.Menu(box)
        for element in self.menu.get_population():
            element.surface = screen

        box.set_topleft((0,502))
        box.blit()
        box.update()
        return

    def proceed_input(self, event):
        self.menu.react(event)


