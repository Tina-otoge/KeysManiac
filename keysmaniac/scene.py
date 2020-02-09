from pyglet.graphics import Batch

class Scene():

    def __init__(self, game=None, context=None):
        self.game = game
        self.batch = Batch()
        self.context = context or {}

    def load(self):
        pass

    def unload(self):
        pass

    def draw(self):
        self.batch.draw()

    def resize(self):
        pass

    def on_key_press(self, symbol, modifiers):
        pass

    def on_key_release(self, symbol, modifiers):
        pass
