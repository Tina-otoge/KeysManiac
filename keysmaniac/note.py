from enum import Enum
from .errors import InvalidBeatDivisorError, InvalidBeatNumeratorError

class Beat:
    def __init__(self, numerator, divisor, n, bpm):
        if numerator < 1:
            raise InvalidBeatNumeratorError(numerator)
        if divisor < 1:
            raise InvalidBeatDivisorError(divisor)
        self.numerator = numerator
        self.divisor = divisor
        self.n = n
        self.bpm = bpm

    def to_time(self):
        time_per_beat = 60 / self.bpm if self.bpm is not 0 else 0
        beat_time = ((self.numerator - 1) / self.divisor) * time_per_beat
        return (time_per_beat * self.n) + beat_time

    def __repr__(self):
        return 'Beat {0.numerator}/{0.divisor}+{0.n}@{0.bpm} ({1}s)'.format(
            self, self.to_time()
        )

class Note:
    def __init__(self, beat, key):
        self.beat = beat
        self.key = key

class LongNote(Note):
    def __init__(self, beat_start, beat_end, key):
        super().__init__(beat_start, key)
        self.beat_end = beat_end

class RepeatNote(Note):
    def __init__(self, beat, key, notes):
        super().__init__(beat, key)
        self.notes = notes
