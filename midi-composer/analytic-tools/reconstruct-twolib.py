from music21 import *
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile
import os



#fp = '../songs/beethoven_movement01.mid'
#fp = '../songs/lbtheme.mid'
#fp = '../songs/world-is-mine.mid'
#fp = './sample0.mid'
fp = '../songs/Suteki-Da-Ne.mid'
#fp = '../songs/how-to-world-domination.mid'

#printTracks = True
#printTracks = False


### Music21 Initalizations
mf = midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()
###

### MIDIUtil Initalizations
MyMIDI = MIDIFile(len(mf.tracks))
duration = 6 	# Controls how long a note is pressed
volume = 100
tempo = 680
###



count = 0
prevPitch = -1

mtf = midi.MidiFile()



mt = midi.MidiTrack(len(mf.tracks))
#mtf.tracks = mt


for tracksNum in range (0, len(mf.tracks)):
    
	print 'Track ', tracksNum

	time = 0
	MyMIDI.addTempo(tracksNum,time,tempo)

	# Prints out the number of events in a track
	numOfEvents = len(mf.tracks[tracksNum].events)


	
	# Begin reconstruction of the track
	for eventInd in range(0,numOfEvents):

		track = mf.tracks[tracksNum].events[eventInd]
		trackType = track.type

		me = midi.MidiEvent(mt)		
		me.type = trackType


		# Tracks
		track = mf.tracks[tracksNum].events[eventInd]
		trackType = track.type

		if printTracks:
			print track


		if trackType == 'NOTE_ON':
		    
		    me.trackType = trackType
		    pitch = track.pitch
		    velocity = track.velocity
		    channel = track.channel
		
		    volume = track.velocity

		    MyMIDI.addNote(tracksNum, channel, pitch, count, duration, volume)
		'''
		if trackType == 'NOTE_OFF':

		    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
		'''


		prevPitch = track.pitch

		count = count + 1


# Writing reconstructed track
print 'Went through ', len(mf.tracks), ' tracks'

binfile = open("result.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()    
