from pyglet import clock

from ..scene import Scene
from ..objects import note_img
from ..display import Grid


class PlayScene(Scene):

    def scroll(self, delta):
        self.time += delta
        print(self.time)

    def load(self):
        self.time = 0
        self.scroll_speed = 100
        clock.schedule_interval(self.scroll, 1 / 120)
        print(clock.get_fps())
        self.simple_note = note_img
        if 'chart' in self.context:
            self.chart = self.context['chart']
            print(self.chart)

    def resize(self):
        self.simple_note.width, self.simple_note.height = Grid(3, 1)

    def draw(self):
        Grid.draw_grid()
        keys = [0, 3, 6, 9]
        for note in self.chart:
            self.simple_note.blit(*Grid(
                3 + keys[note.key - 1], 1,
                offset_y=(note.beat.to_time() - self.time) * self.scroll_speed
            ))
