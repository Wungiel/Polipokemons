class GameState(object):

    def __init__(self):
        self.done = False
        self.mode = 'map'

    def changeState(self):
        self.done = True

    def changeMode(self):
        if self.mode == 'map':
            self.mode = 'battle'
        else:
            self.mode = 'map'