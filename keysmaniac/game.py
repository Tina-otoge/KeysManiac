from pyglet.window import Window
from pyglet.app import run

from .log import logging
from .scenes.play import PlayScene

class Game():

    def __init__(self):
        self.window = Window()
        self.window.push_handlers(self)
        self.scene = None

    def load_scene(self, scene_class):
        new_scene = scene_class()
        if self.scene:
            new_scene.context = self.scene.context
            self.scene.unload()
        self.scene = new_scene

    def on_draw(self):
        if not self.scene:
            logging.warning('No scene has been loaded')
            return
        self.window.clear()
        self.scene.draw()
