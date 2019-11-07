from pyglet.graphics import Batch

class Scene():

    def __init__(self, game=None, context=None):
        self.game = game
        self.batch = Batch()
        self.context = context or {}

    def resize(self):
        pass

    def draw(self):
        self.batch.draw()

    def load(self):
        pass

    def unload(self):
        pass
