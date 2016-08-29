from music21 import converter,instrument # or import *
s = converter.parse('../songs/world-is-mine.mid')
#s = converter.parse('../songs/beethoven_movement01.mid')

for el in s.recurse():
    if 'Instrument' in el.classes: # or 'Piano'
        el.activeSite.replace(el, instrument.Violin())

s.write('midi', '../violin_result.mid')
