from ..scene import Scene
from ..objects import note_img

class PlayScene(Scene):
    def __init__(self):
        self.simple_note = note_img

    def draw(self):
        c = range(5, 1000, 20)
        b = range(5, 1000, 20)
        for y in range(1, 20, 8):
            for x in range(1, 5):
                self.simple_note.blit(c[x], b[x + y])
            for x in range(1, 4):
                self.simple_note.blit(c[4 - x], b[x + y + 4])
