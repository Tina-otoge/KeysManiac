from pyglet import resource

resource.path = ['./resources']
resource.reindex()

note_img = resource.image('note.png')
