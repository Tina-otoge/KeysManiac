from dataclasses import dataclass
from typing import List, Optional, Tuple
from pyglet.graphics import OrderedGroup
from pyglet.shapes import Rectangle
from pyglet.text import Label

import km2
from km2.event import Event
from km2.utils import colors

@dataclass
class Selectable:
    active: bool = False

    def set_active(self, state: bool):
        self.active = state
        if state:
            self.on_activate()
        else:
            self.on_deactivate()

    def on_activate(self):
        pass

    def on_deactivate(self):
        pass

    def on_confirm(self):
        pass

@dataclass
class Browsable(Selectable):
    left: Optional[Selectable] = None
    down: Optional[Selectable] = None
    up: Optional[Selectable] = None
    right: Optional[Selectable] = None

class MenuText(Browsable):
    def __init__(self, text, x, y, w=100, h=40, scene=None, on_confirm=None):
        self.on_confirm_default = (on_confirm,)
        batch = scene.batch
        self.scene = scene
        background = OrderedGroup(0)
        foreground = OrderedGroup(1)
        self.active_bg = Rectangle(
            x, y, w, h, colors.GREEN, batch=batch, group=background
        )
        self.active_bg.visible = False
        self.inactive_bg = Rectangle(
            x, y, w, h, colors.GRAY, batch=batch, group=background
        )
        y_center = h / 2 + y
        self.text = Label(
            text,
            x=x, y=y_center,
            width=w, height=h,
            # anchor_x='center',
            align='center',
            batch=batch,
            group=foreground,
        )

    def on_activate(self):
        self.active_bg.visible = True
        self.inactive_bg.visible = False

    def on_deactivate(self):
        self.active_bg.visible = False
        self.inactive_bg.visible = True

    def on_confirm(self):
        if self.on_confirm_default:
            self.on_confirm_default[0]()

@dataclass
class Menu:
    def __init__(self, active: Browsable):
        self.active = active
        self.active.set_active(True)

    def handle(self, event: Event):
        if event.action == Event.Action.CONFIRM:
            return self.active.on_confirm()
        if not event.is_direction:
            return
        direction_str = event.action.name.lower()
        if not (to := getattr(self.active, direction_str)):
            return
        self.active.set_active(False)
        self.active = to
        self.active.set_active(True)
        km2.logger.debug(f'Selected {to}')

    @classmethod
    def from_map(cls, map: List[List[Browsable]], active: Tuple[int, int]):
        for y in range(len(map)):
            for x, elem in enumerate(map[y]):
                if y > 0:
                    elem.up = map[y - 1][x]
                if x > 0:
                    elem.left = map[y][x - 1]
                if y < len(map) - 1:
                    elem.down = map[y + 1][x]
                if x < len(map[y]) - 1:
                    elem.right = map[y][x + 1]
        return cls(active=map[active[1]][active[0]])
