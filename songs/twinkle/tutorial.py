from pathlib import Path

from keysmaniac.note import Beat, Note

notes_4 = [1, 1, 2, 2, 3, 3, 4, 0, 4, 4, 3, 3, 2, 2, 1, 0]
bpm = 80

def gen_chart():
    result = []
    for n in range(0, len(notes_4)):
        if notes_4[n] == 0:
            continue
        beat = Beat(4 + n, 4, bpm)
        note = Note(beat, notes_4[n])
        result.append(note)
    return result

package = {
    'song': {
        'title': 'Twinkle Twinkle Little Star (Instrumental)',
        'artist': 'The Green Orbs',
        'timings': {0: bpm},
    },
    'chart': gen_chart(),
    'meta': {
        'path': Path(__file__).parent,
        'audio': 'twinkle.ogg'
    }
}
