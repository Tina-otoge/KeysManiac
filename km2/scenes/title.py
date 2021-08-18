from pyglet import media
from pyglet.media import Player
from pyglet.text import Label

import km2
from km2.scene import Scene


class Title(Scene):
    def open(self):
        size = 30
        margin = 4
        self.title_text = Label(
            text='Welcome to KM2',
            font_name='Symtext',
            x=self.game.center.x,
            y=self.game.height - size - margin,
            anchor_x='center',
            bold=True,
            font_size=size,
            batch=self.batch
        )
        small_size = size * 0.75
        self.sub_text = Label(
            text='Press any key',
            font_size=small_size,
            x=self.game.center.x,
            y=self.game.height - size - small_size - (margin * 3),
            anchor_x='center',
            batch=self.batch,
        )
        self.bga = Player()
        self.bga.loop = True
        try:
            source = media.load('./resources/background.mp4')
        except FileNotFoundError as e:
            km2.logger.warning(e)
        else:
            self.bga.queue(source)
            self.bga.play()

    def close(self):
        self.bga.delete()

    def before_draw(self):
        if self.bga.playing:
            self.bga.texture.blit(
                0, 0, width=self.game.width, height=self.game.height
            )

    def handle(self, event):
        self.game.load_scene('MainMenu')
