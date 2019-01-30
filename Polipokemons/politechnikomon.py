import pygame

class Politechnikomon(object):

    def __init__(self, pokemon_file, name, strenght):
        self.pokemon_graphics = pygame.image.load(pokemon_file).convert_alpha()   
        self.pokemon_graphics = pygame.transform.scale(self.pokemon_graphics,(200,200))
        self.maxHealth = 200
        self.name = name
        self.strenght = strenght

