from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float


class HasCenterMixin:
    width: float
    height: float

    @property
    def center(self):
        return Point(self.width // 2, self.height // 2)
