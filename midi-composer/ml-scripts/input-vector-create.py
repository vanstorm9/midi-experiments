# Used to form the song input vector that we will used as input for model.py

import music21
import matplotlib.pyplot as plt
import numpy as np
import os

matrix_path = "../matrices/input/"
slash = "/"
dash = "-"

#fp = '../songs/beethoven_movement01.mid'
#fp = '../songs/world-is-mine.mid'
#fp = '../songs/how-to-world-domination.mid'
fp = '../songs/Suteki-Da-Ne.mid'

#name = "world-is-mine"
#name = "how-to-world-domination"
name = "suteki-da-ne"


mf = music21.midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()


x = []
y = []

mainCounter = 0
prevPitch = 0

for tracksNum in range (0, len(mf.tracks)):
    # Prints out the number of events in a track
    numOfEvents = len(mf.tracks[tracksNum].events)
    print numOfEvents
    
    count = 0
    for eventInd in range(0,numOfEvents):
        
        # Tracks
        track = mf.tracks[tracksNum].events[eventInd]
        trackType = track.type

        if trackType == 'NOTE_ON':
            #print track
	    if prevPitch != track.pitch:
                y.append(track.pitch)
                x.append(count)
                count = count + 1
        '''
        elif trackType == 'NOTE_OFF':
            print track
        '''
      
    save_path = matrix_path + name + slash + name 
    x_set = '-x-' + str(mainCounter) + '.npy'
    y_set = '-y-' + str(mainCounter) + '.npy'
    
    np.save(save_path + x_set , x)
    np.save(save_path + y_set , y)
 
    plt.plot(x,y,'ro')
    plt.show()

    x = []
    y = []
            
    mainCounter = mainCounter + 1
        
    


