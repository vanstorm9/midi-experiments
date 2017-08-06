from music21 import *
import matplotlib.pyplot as plt
from midiutil.MidiFile import MIDIFile
import os



#fp = '../songs/beethoven_movement01.mid'
#fp = '../songs/lbtheme.mid'
fp = '../songs/world-is-mine.mid'
#fp = './sample0.mid'
#fp = '../songs/Suteki-Da-Ne.mid'
#fp = '../songs/how-to-world-domination.mid'

printTracks = False

# Setting up new midi file
MyMIDI = MIDIFile(1)
track = 0
time = 0
channel = 0
duration = 6 	# Controls how long a note is pressed
volume = 100
tempo = 680


MyMIDI.addTrackName(track, time, "Sample Track")
MyMIDI.addTempo(track,time,tempo)

### Music21 Initalizations
mf = midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()
###


count = 0
prevPitch = -1

mtf = midi.MidiFile()

for tracksNum in range (0, len(mf.tracks)):
    
	print 'Track ', tracksNum

	# Prints out the number of events in a track
	numOfEvents = len(mf.tracks[tracksNum].events)

	mt = midi.MidiTrack(1)
	mtf.tracks = mt

	
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
