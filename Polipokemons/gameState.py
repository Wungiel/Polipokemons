class GameState(object):

    def __init__(self):
        self.done = False

    def changeState(self):
        self.done = True