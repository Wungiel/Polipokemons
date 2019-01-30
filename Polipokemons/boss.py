import pygame

class Boss(object):
    tile_size = 40

    def __init__(self, boss_file,):
        self.boss_graphics = pygame.image.load(boss_file).convert_alpha()   
        self.boss_face = pygame.image.load('boss_face.png').convert_alpha()
        self.position = [5,5]
        self.text = ["Niemądry studencie", "Naprawdę myślisz że wygrasz..." , "WALKĘ POLITECHNIKOMONÓW?", "Przyjmuję twoje wyzwanie!"]
        self.speakCounter = 0

    def draw_boss(self, screen):
        screen.blit(self.boss_graphics, (self.position[0]*Boss.tile_size, self.position[1]*Boss.tile_size))

    def check_movement(self, movement, player_position):
        x = movement[0]+player_position[0]
        y = movement[1]+player_position[1] 
        if (self.position[0] == x) and (self.position[1] == y):
            return False
        else:
            return True

    def speak(self, screen, gui):
        if (self.speakCounter < 4):
            screen.blit(self.boss_face, (300, 100))
            gui.show_text(self.text[self.speakCounter])

    def speakCounterIncrement(self):
        self.speakCounter += 1


