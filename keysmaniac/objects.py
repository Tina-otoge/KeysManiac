from .errors import InvalidBeatDivisorError, InvalidBeatNumeratorError
from .rules import NORMAL_WINDOW, BONUS_WINDOW, BONUS, MISS

class TimingPoint:
    def __init__(self, n, divisor, bpm):
        if n < 1:
            raise InvalidBeatNumeratorError(numerator)
        if divisor < 1:
            raise InvalidBeatDivisorError(divisor)
        self.n = n
        self.divisor = divisor
        self.numerator = n % self.divisor
        self.bpm = bpm
        self.time = self.numerator // self.divisor

    def to_seconds(self):
        time_per_beat = 60 / self.bpm if self.bpm is not 0 else 0
        beat_time = ((self.n - 1) / self.divisor) * time_per_beat
        return time_per_beat + beat_time

    def __repr__(self):
        return 'TimingPoint {0.numerator}/{0.divisor}+{0.n}@{0.bpm} ({1}s)'.format(
            self, self.to_seconds()
        )

class TimedObject:
    def __init__(self, timing_point=None):
        self.timing_point = timing_point
        self.delta = None

    def update(self, time):
        self.delta = time - self.get_time()

    def get_time(self):
        return self.timing_point.to_seconds()

    def get_delta(self, time):
        return time - self.get_time()

class DurationObject(TimedObject):
    def __init__(self, timing_point_end=None, **kwargs):
        super().__init__(**kwargs)
        self.timing_point_end = timing_point_end

    def get_end_time(self):
        return self.timing_point_end.to_seconds()

class BGA(DurationObject):
    def __init__(self, video=None, **kwargs):
        super().__init__(**kwargs)
        self.video = video

class BGM(DurationObject):
    def __init__(self, audio=None, **kwargs):
        super().__init__(**kwargs)
        self.audio = audio

class Note(TimedObject):
    def __init__(self, key_sound=None, auto=False, **kwargs):
        super().__init__(**kwargs)
        self.key_sound = key_sound
        self.auto = auto
        self.window = NORMAL_WINDOW
        self.miss = MISS
        self.judge = None
        self.force_hit = False
        self.hit_at = None

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self.judge = self.get_judge_state()
        self.force_hit = self.get_force_state()

    def get_force_state(self):
        return self.judge is MISS or (self.auto and self.delta >= 0)

    def get_judge_state(self):
        if self.delta > self.window[-1].TIMING:
            return self.miss
        delta = abs(self.delta)
        for judge in self.window:
            if delta <= judge.TIMING:
                return judge
        return None

    def is_hittable(self):
        return self.judge is not None

class SimpleNote(Note):
    def __init__(self, key=None, **kwargs):
        super().__init__(**kwargs)
        self.score = 0
        self.key = key

class LongNote(SimpleNote, DurationObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class TrickNote(SimpleNote):
    def __init__(self, notes=None, **kwargs):
        super().__init__(**kwargs)
        self.notes = notes

class SimpleMine(SimpleNote):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window = BONUS_WINDOW

    def get_force_state(self):
        return self.judge == BONUS

    def get_judge_state(self, time):
        delta = self.get_delta(time)
        if delta > self.window[-1]:
            return BONUS
        delta = abs(delta)
        for judge in self.window:
            if delta <= judge.TIMING:
                return MISS
        return None

class LongMine(LongNote, SimpleMine):
    pass

class GhostNote(Note):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.window = BONUS_WINDOW
        self.miss = None

