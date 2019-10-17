from pyglet.app import run

from keysmaniac.game import Game
from keysmaniac.scenes import PlayScene

game = Game()
game.load_scene(PlayScene)
run()
