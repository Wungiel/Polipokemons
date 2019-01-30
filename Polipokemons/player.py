import pygame

class Player(object):
    tile_size = 40

    def __init__(self, player_file,):
        self.player_graphics = pygame.image.load(player_file).convert_alpha()   
        self.position = [6,6]

    def move_player(self, movement):
        self.position[0] += movement[0]
        self.position[1] += movement[1]

    def draw_player(self, screen):
        screen.blit(self.player_graphics, (self.position[0]*Player.tile_size, self.position[1]*Player.tile_size))



