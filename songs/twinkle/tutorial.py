from pathlib import Path

from keysmaniac.objects import TimingPoint, SimpleNote

notes_4 = [1, 1, 2, 2, 3, 3, 4, 0, 4, 4, 3, 3, 2, 2, 1, 0]
bpm = 80

def gen_chart():
    result = []
    for n in range(0, len(notes_4)):
        if notes_4[n] == 0:
            continue
        beat = TimingPoint(17 + n, 1, bpm)
        note = SimpleNote(timing_point=beat, key=notes_4[n])
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
