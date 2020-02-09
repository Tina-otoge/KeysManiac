from pyglet import clock, media
from pyglet.sprite import Sprite
from pyglet.text import Label
from pyglet.window import key

from ..log import logger
from ..scene import Scene
from ..resources import note_img, judgeline_img, judge_imgs, keypressed_img, scorebox_img, fast_img, slow_img
from ..rules import NormalJudgement, BonusJudgement, MISS, HAS_DELTA
from ..display import Grid


class PlayScene(Scene):

    def load(self):
        self.score = 0
        self.combo = 0
        self.bonus_score = 0
        self.time = 0.5
        self.scroll_speed = 30
        self.package = self.context.get('song')
        self.playing_notes = self.package['chart'].copy()
        self.playing_notes.sort(key=lambda x: x.get_time(), reverse=True)
        self.judged_notes = []
        self.last_hit = None
        self.lanes_state = [False] * 4
        self.score_label = Label(self.build_score_string(), None, font_size=12)
        self.combo_label = Label(self.build_combo_string(), 'monospace', font_size=Grid.get_unit(1), anchor_x='center')
        bgm = media.load(str(self.package['meta']['path'] / self.package['meta']['audio']))
        clock.schedule_interval(self.scroll, 1 / 120)
        bgm.play()

    def draw(self):
        Grid.draw_grid()
        factor = Grid.get_unit()
        columns_position = [3, 6, 9, 12]
        judgeline_img.blit(*Grid(3, 1))
        scorebox_img.blit(*Grid(18, 4))
        self.score_label.draw()
        if self.combo >= 5:
            self.combo_label.draw()
        if self.last_hit and self.last_hit.hit_at + 1 > self.time:
            judge_imgs[self.last_hit.judge].blit(*Grid(4, 4))
            if self.last_hit.judge in HAS_DELTA:
                delta_img = fast_img if self.last_hit.delta < 0 else slow_img
                delta_img.blit(*Grid(7, 6))
        for lane, state in enumerate(self.lanes_state):
            if state:
                keypressed_img.blit(*Grid((lane * 3) + 3, 1))
        for note in self.playing_notes:
            note.update(self.time)
            note_img.blit(*Grid(
                columns_position[note.key - 1], 1,
                offset_y=(note.get_time() - self.time) * self.scroll_speed * factor
            ))
            if note.force_hit:
                self.hit(note)

    def resize(self):
        note_img.width, note_img.height = Grid(3, 1)
        judgeline_img.width, judgeline_img.height = Grid(12, 1)
        for judge in judge_imgs.values():
            judge.width, judge.height = Grid(10, 2)
        fast_img.width, fast_img.height = Grid(4, 1)
        slow_img.width, slow_img.height = Grid(4, 1)
        keypressed_img.width, keypressed_img.height = Grid(3, 1)
        scorebox_img.width, scorebox_img.height = 150, 24
        self.score_label.x, self.score_label.y = Grid(18, 4, 16, 6)
        self.combo_label.x, self.combo_label.y = Grid(9, 30)

    def on_key_press(self, symbol, modifiers):
        lane = self.get_key_lane(symbol)
        if not lane:
            return
        self.lanes_state[lane - 1] = True
        self.keys_hit(lane)

    def on_key_release(self, symbol, modifiers):
        lane = self.get_key_lane(symbol)
        if not lane:
            return
        self.lanes_state[lane - 1] = False


    def scroll(self, delta):
        self.time += delta

    def note_delta(self, note):
        return self.time - note.timing_point.to_seconds()

    def get_key_lane(self, pressed):
        mapping = {key.S: 1, key.D: 2, key.K: 3, key.L: 4}
        if pressed in mapping:
            return mapping[pressed]
        return None

    def keys_hit(self, lane):
        for note in reversed(self.playing_notes):
            if not note.is_hittable():
                break
            if note.key == lane:
                self.hit(note)
                break

    def hit(self, note):
        self.playing_notes.remove(note)
        note.hit_at = self.time
        self.last_hit = note
        self.score += note.judge.SCORE
        self.bonus_score += note.judge.BONUS_SCORE
        if note.judge is MISS:
            self.combo = 0
        else:
            self.combo += 1
        self.score_label.text = self.build_score_string()
        self.combo_label.text = self.build_combo_string()
        self.judged_notes.append(note)

    def build_score_string(self):
        return 'Score: ' + '{0:.1f}'.format(self.score).zfill(6)

    def build_combo_string(self):
        return str(self.combo).zfill(4)
