from typing import Optional, Type, Union
import pyglet
from pyglet.window import Window

import km2
from km2.event import Event, KeyPress
from km2.scene import Scene
from km2.utils.geometry import HasCenterMixin

class SimplerWindow(Window, HasCenterMixin):
    pass


class Game(SimplerWindow):
    def __init__(self):
        self.events = []
        self.scene: Optional[Scene] = None
        Window.__init__(self, resizable=False)
        km2.setup_logger()
        km2.setup_fonts()

    def run(self):
        self.load_scene('Title')
        pyglet.app.run()

    @staticmethod
    def exit():
        pyglet.app.exit()

    def load_scene(self, scene: Union[Type[Scene], str], *args, **kwargs):
        if self.scene:
            km2.logger.debug(f'Closing scene {self.scene}')
            self.scene.close()
            self.scene = None
        if isinstance(scene, str):
            scene = Scene.by_name(scene)
        km2.logger.debug(f'Opening scene {scene}')
        self.scene = scene(self)
        self.scene.open(*args, **kwargs)

    def on_draw(self):
        try:
            while self.events:
                self.scene.handle(self.events.pop())
            self.clear()
            self.scene.before_draw()
            self.scene.batch.draw()
            self.scene.after_draw()
        except Exception:
            km2.logger.exception('Error during draw')
            self.load_scene('Title')

    def on_key_press(self, symbol, modifier):
        raw = KeyPress(symbol, modifier)
        event = Event.from_raw_event(raw)
        self.events.append(event)
