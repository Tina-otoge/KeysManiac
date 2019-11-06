from .errors import InvalidBeatDivisorError, InvalidBeatNumeratorError

class Judge:
    TIMINGS = [
        0.017,
        0.03,
        0.05
    ]
    WEIGHTS = [
        1,
        0.5,
        0.2
    ]
    MISS = 0

    @classmethod
    def evaluate(cls, delta):
        delta = abs(delta)
        for result, timing in enumerate(cls.TIMINGS, start=cls.MISS + 1):
            if delta <= timing:
                return result
        return cls.MISS

    @classmethod
    def is_out(cls, delta):
        return delta > cls.TIMINGS[-1]

    @classmethod
    def weight(cls, judge):
        try:
            return cls.WEIGHTS[judge - (cls.MISS + 1)]
        except IndexError:
            return cls.MISS




class Beat:
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

    def to_time(self):
        time_per_beat = 60 / self.bpm if self.bpm is not 0 else 0
        beat_time = ((self.n - 1) / self.divisor) * time_per_beat
        return time_per_beat + beat_time

    def __repr__(self):
        return 'Beat {0.numerator}/{0.divisor}+{0.n}@{0.bpm} ({1}s)'.format(
            self, self.to_time()
        )

class Note:
    def __init__(self, beat, key, *, key_sound=None, auto=False):
        self.beat = beat
        self.key = key
        self.score = None
        self.key_sound = key_sound
        self.auto = auto

class LongNote(Note):
    def __init__(self, beat_start, beat_end, key):
        super().__init__(beat_start, key)
        self.beat_end = beat_end

class RepeatNote(Note):
    def __init__(self, beat, key, notes):
        super().__init__(beat, key)
        self.notes = notes
