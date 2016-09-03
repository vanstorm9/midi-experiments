import music21
import matplotlib.pyplot as plt
import os

#fp = '../songs/beethoven_movement01.mid'
fp = '../songs/world-is-mine.mid'
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
    
    count = 0
    prevPitch = -1

    for eventInd in range(0,numOfEvents):
        
        # Tracks
        track = mf.tracks[tracksNum].events[eventInd]
        trackType = track.type

        if trackType == 'NOTE_ON':
            #print track
		if prevPitch != track.pitch:
			y.append(track.pitch)
			x.append(count)

			prevPitch = track.pitch

			count = count + 1
        '''
        elif trackType == 'NOTE_OFF':
            print track
        '''
        
    plt.plot(x,y,'ro')
    plt.show()

    x = []
    y = []
            

        
    


