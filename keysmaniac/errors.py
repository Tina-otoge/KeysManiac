class KeysManiacException(Exception):
    pass

class MusicCorrectnessError(KeysManiacException):
    pass

class InvalidBeatDivisorError(MusicCorrectnessError):
    def __init__(self, value=None):
        msg = 'Invalid beat divisor'
        if value:
            msg += ' {}'.format(value)
        super().__init__(msg)

class InvalidBeatNumeratorError(MusicCorrectnessError):
    def __init__(self, value=None):
        msg = 'Invalid beat numerator'
        if value:
            msg += ' {}'.format(value)
        super().__init__(msg)
