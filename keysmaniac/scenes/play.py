from pyglet import clock, media

from ..log import logger
from ..note import Judge
from ..scene import Scene
from ..objects import note_img, judgeline_img
from ..display import Grid


class PlayScene(Scene):

    def scroll(self, delta):
        self.time += delta

    def load(self):
        self.time = 0
        self.scroll_speed = 30
        clock.schedule_interval(self.scroll, 1 / 120)
        self.simple_note = note_img
        self.judgeline = judgeline_img
        self.package = self.context.get('song')
        self.playing_notes = self.package['chart'].copy()
        self.judged_notes = []
        bgm = media.load(str(self.package['meta']['path'] / self.package['meta']['audio']))
        bgm.play()

    def resize(self):
        self.simple_note.width, self.simple_note.height = Grid(3, 1)
        self.judgeline.width, self.judgeline.height = Grid(12, 1)

    def draw(self):
        Grid.draw_grid()
        factor, _ = Grid.factor
        keys = [0, 3, 6, 9]
        self.judgeline.blit(*Grid(3, 1))
        for note in self.playing_notes:
            if Judge.is_out(self.time - note.beat.to_time()):
                logger.debug('missed')
                note.score = Judge.MISS
                self.judged_notes.append(note)
                self.playing_notes.remove(note)
                continue
            self.simple_note.blit(*Grid(
                3 + keys[note.key - 1], 1,
                offset_y=(note.beat.to_time() - self.time) * self.scroll_speed * factor
            ))
