import pygame

class Map(object):

    tile_size = 40

    def __init__(self, map_file, tile_file):
        self.map_file = map_file
        self.tile_file = tile_file
        self.map_matrix = [[0 for x in range(100)] for y in range(100)] 

        tiles = pygame.image.load(self.tile_file).convert()        
        
        self.tile_table = []
        for x in range(0, 3):
                rect = (x*Map.tile_size, 0, Map.tile_size, Map.tile_size)
                self.tile_table.append(tiles.subsurface(rect))

    def generate_map(self):        
        map = pygame.image.load(self.map_file)    
        self.map_width, self.map_height = map.get_size()
        for x in range (self.map_width-1):
            for y in range (self.map_height-1):
                color = map.get_at((x,y))
                if color[0] == 255:
                    self.map_matrix[x][y]='r'
                if color[1] == 255:
                    self.map_matrix[x][y]='g'
                if color[2] == 255:
                    self.map_matrix[x][y]='b'

    def draw_map(self, screen, position):
        for x in range (self.map_width-1):
            for y in range (self.map_height-1):
                if self.map_matrix[x][y]=='r':
                    tile = self.tile_table[0]
                if self.map_matrix[x][y]=='g':
                    tile = self.tile_table[2]
                if self.map_matrix[x][y]=='b':
                    tile = self.tile_table[1]
                screen.blit(tile, (x*Map.tile_size - position[0],y*Map.tile_size- position[1]))



