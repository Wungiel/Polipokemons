import pygame

class Battle(object):

    def __init__(self, leftPokemon, rightPokemon):
        self.leftRect = pygame.Rect(000,280,200,200)
        self.rightRect = pygame.Rect(600,280,200,200)
        self.leftHealthRect = pygame.Rect(000,250,200,200)
        self.rightHealthRect = pygame.Rect(600,250,200,200)
        self.leftNameRect = pygame.Rect(000,230,200,200)
        self.rightNameRect = pygame.Rect(600,230,200,200)
        self.leftPokemon = leftPokemon
        self.rightPokemon = rightPokemon
        self.leftHealth = self.leftPokemon.maxHealth
        self.rightHealth = self.rightPokemon.maxHealth
        self.font = pygame.font.SysFont("monospace", 20)

    def drawBattle(self,screen):
        screen.blit(self.leftPokemon.pokemon_graphics, self.leftRect)
        screen.blit(pygame.transform.flip(self.rightPokemon.pokemon_graphics, True, False), self.rightRect)

        screen.blit(self.font.render(str(self.leftHealth),1,(0,0,0)), self.leftHealthRect)
        screen.blit(self.font.render(str(self.rightHealth),1,(0,0,0)), self.rightHealthRect)

        screen.blit(self.font.render(str(self.leftPokemon.name),1,(0,0,0)), self.leftNameRect)
        screen.blit(self.font.render(str(self.rightPokemon.name),1,(0,0,0)), self.rightNameRect)

    def checkBattleState(self):
        if (self.rightHealth <= 0):
            self.leftPokemon.maxHealth += 10
            self.leftPokemon.strenght += 10
            return 'victory'
        elif (self.leftHealth <= 0):
            return 'defeat'
        else:
            return 'continue'

    def attackEnemy(self):
        self.rightHealth -= self.leftPokemon.strenght
        self.leftHealth -= self.rightPokemon.strenght
