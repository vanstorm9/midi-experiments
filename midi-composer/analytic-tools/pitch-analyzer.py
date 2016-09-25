import music21
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile
import os



#fp = '../songs/beethoven_movement01.mid'
fp = '../songs/world-is-mine.mid'
#fp = './sample0.mid'
#fp = '../songs/Suteki-Da-Ne.mid'
#fp = '../songs/how-to-world-domination.mid'

tracknum = 1

mf = music21.midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()


x = []
y = []

for tracksNum in range (0, len(mf.tracks)):
    # Prints out the number of events in a track
    numOfEvents = len(mf.tracks[tracksNum].events)
    print numOfEvents
    print mf.tracks
    
    count = 0
    prevPitch = -1

    for eventInd in range(0,numOfEvents):
        # Tracks
        track = mf.tracks[tracksNum].events[eventInd]
        trackType = track.type

        if trackType == 'NOTE_ON':
            y.append(track.pitch)
            x.append(count)

        prevPitch = track.pitch

        count = count + 1
    


    '''
    ################################
    MyMIDI = MIDIFile(1)
    track = 0
    time = 0
    channel = 0
    duration = 1
    volume = 100
    tempo = 520

    MyMIDI.addTrackName(track, time, "Sample Track")
    MyMIDI.addTempo(track,time,tempo)

    for i in range(0,len(x)-1):
        time = x[i]
        pitch = y[i]

        MyMIDI.addNote(track, channel, pitch, time, duration, volume)

    binfile = open("result.mid", 'wb')
    MyMIDI.writeFile(binfile)
    binfile.close()    
    ################################
    '''

    plt.plot(x,y,'ro')
    plt.show()

    x = []
    y = []
            

        
    


