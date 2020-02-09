from pyglet import resource
from .rules import JUDGES

resource.path = ['./resources']
resource.reindex()

note_img = resource.image('note.png')
keypressed_img = resource.image('key-pressed.png')
judgeline_img = resource.image('judgeline.png')

judge_imgs = {judge: resource.image('judges/{}.png'.format(judge.NAME.lower())) for judge in JUDGES}
fast_img = resource.image('judges/fast.png')
slow_img = resource.image('judges/slow.png')

scorebox_img = resource.image('score-box.png')
