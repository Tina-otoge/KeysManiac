from pyglet.app import run

from keysmaniac.game import Game
from keysmaniac.scenes import PlayScene
from keysmaniac.scene import Scene
from songs.twinkle.tutorial import package

class DummyScene(Scene):
    pass

game = Game()
game.scene = DummyScene()
game.scene.context['song'] = package
game.load_scene(PlayScene)
run()
