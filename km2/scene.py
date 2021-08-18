from pyglet.graphics import Batch


class Scene:
    def __init__(self, game):
        self.game = game
        self.batch = Batch()

    def __del__(self):
        self.close()

    @classmethod
    def by_name(cls, name: str):
        return {x.__name__: x for x in cls.__subclasses__()}[name]

    def open(self):
        pass

    def close(self):
        pass

    def handle(self, event):
        pass

    def before_draw(self):
        pass

    def after_draw(self):
        pass
