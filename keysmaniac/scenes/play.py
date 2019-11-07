from pyglet import clock, media
from pyglet.window import key

from ..log import logger
from ..scene import Scene
from ..resources import note_img, judgeline_img
from ..rules import NormalJudgement, BonusJudgement
from ..display import Grid


class PlayScene(Scene):

    def scroll(self, delta):
        self.time += delta

    def note_delta(self, note):
        return self.time - note.timing_point.to_seconds()

    def get_keys(self):
        result = []
        mapping = {key.S: 1, key.D: 2, key.K: 3, key.L: 4}
        for bound, action in mapping.items():
            if self.game.keys[bound]:
                result.append(action)
        return result

    def keys_hit(self, notes):
        key_presses = self.get_keys()
        if key_presses:
            print('pressing:', key_presses)
        for note in notes:
            if note.key in key_presses:
                key_presses.remove(note.key)
                self.hit(note)

    def hit(self, note):
        self.playing_notes.remove(note)
        note.hit_at = self.time
        print('hit! judge:', note.judge)
        print('score:', self.score)
        self.score += note.judge.SCORE
        self.bonus_score += note.judge.BONUS_SCORE
        self.judged_notes.append(note)

    def load(self):
        self.score = 0
        self.bonus_score = 0
        self.time = 0.5
        self.scroll_speed = 30
        self.simple_note = note_img
        self.judgeline = judgeline_img
        self.package = self.context.get('song')
        self.playing_notes = self.package['chart'].copy()
        self.judged_notes = []
        bgm = media.load(str(self.package['meta']['path'] / self.package['meta']['audio']))

        clock.schedule_interval(self.scroll, 1 / 120)
        bgm.play()

    def resize(self):
        self.simple_note.width, self.simple_note.height = Grid(3, 1)
        self.judgeline.width, self.judgeline.height = Grid(12, 1)

    def draw(self):
        Grid.draw_grid()
        factor, _ = Grid.factor
        columns_position = [3, 6, 9, 12]
        self.judgeline.blit(*Grid(3, 1))
        hittable_notes = []
        for note in self.playing_notes:
            note.update(self.time)
            self.simple_note.blit(*Grid(
                columns_position[note.key - 1], 1,
                offset_y=(note.get_time() - self.time) * self.scroll_speed * factor
            ))
            if note.force_hit:
                self.hit(note)
            elif note.is_hittable():
                hittable_notes.append(note)
        hittable_notes.sort(key=lambda x: x.get_time(), reverse=True)
        self.keys_hit(hittable_notes)
