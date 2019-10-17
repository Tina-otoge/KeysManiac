from pyglet.graphics import Batch

class Scene():

    def __init__(self):
        self.batch = Batch()
        self.load()

    def draw(self):
        self.batch.draw()

    def load(self):
        pass

    def unload(self):
        pass
