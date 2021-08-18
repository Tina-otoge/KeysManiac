from pyglet.gui import WidgetBase, PushButton
from pyglet.shapes import Rectangle

from km2.event import Event
from km2.scene import Scene


class MainMenu(Scene):
    def handle(self, event):
        if event.action == Event.Action.CANCEL:
            self.game.load_scene('Title')

    def open(self):
        pass
