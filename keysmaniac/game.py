from pyglet import gl
from pyglet.window import Window
from pyglet.app import run

from .display import Grid
from .log import logging
from .scenes.play import PlayScene

class Game():

    def __init__(self):
        gl.glEnable(gl.GL_TEXTURE_2D)
        gl.glTexParameteri(gl.GL_TEXTURE_2D, gl.GL_TEXTURE_MAG_FILTER, gl.GL_NEAREST)
        self.window = Window(width=640, height=360)
        Grid.set_factor_from_resolution(*self.window.get_size())
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

    def on_resize(self, width, height):
        Grid.set_factor_from_resolution(width, height)
        self.scene.resize()

    def on_activate(self):
        self.on_draw()
