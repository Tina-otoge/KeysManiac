from dataclasses import dataclass
from datetime import datetime
import enum
from pyglet.window import key


class RawEvent:
    pass

@dataclass
class KeyPress(RawEvent):
    symbol: int
    modifier: int


class Event:
    class Action(enum.Enum):
        CONFIRM = enum.auto()
        CANCEL = enum.auto()
        LEFT = enum.auto()
        DOWN = enum.auto()
        UP = enum.auto()
        RIGHT = enum.auto()

    def __init__(self, action: Action = None):
        self.action = action
        self.time = datetime.now()

    def __repr__(self):
        return f'<{self.__class__.__name__} {str(self)}>'

    def __str__(self):
        return f'{self.action} @ {self.time}'

    @classmethod
    def from_raw_event(cls, event: RawEvent):
        if not isinstance(event, KeyPress):
            return
        mapping = {
            key.ENTER: cls.Action.CONFIRM,
            key.BACKSPACE: cls.Action.CANCEL,
            key.ESCAPE: cls.Action.CANCEL,
            key.LEFT: cls.Action.LEFT,
            key.DOWN: cls.Action.DOWN,
            key.UP: cls.Action.UP,
            key.RIGHT: cls.Action.RIGHT,
        }
        return cls(action=mapping.get(event.symbol))
