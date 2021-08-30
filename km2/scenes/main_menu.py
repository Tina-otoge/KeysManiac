from km2.event import Event
from km2.scene import Scene
from km2.utils import ui


class MainMenu(Scene):
    def handle(self, event):
        if event.action == Event.Action.CANCEL:
            self.game.load_scene('Title')
        self.menu.handle(event)

    def open(self):
        def e(text, x, y, f=None):
            return ui.MenuText(text, x, y, on_confirm=f, scene=self)
        def f_scene(scene):
            def result():
                self.game.load_scene(scene)
            return result
        self.menu = ui.Menu.from_map([
            [
                e('Music select', 10, 10, f=f_scene('MusicSelect')),
                e('Options', 120, 10, f=f_scene('Options')),
                e('Quit', 230, 10, f=self.game.exit)],
        ], (0, 0))
