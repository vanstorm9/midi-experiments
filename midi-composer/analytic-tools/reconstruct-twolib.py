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

#printTracks = True
printTracks = False

programChangeOn = False

### Music21 Initalizations
mf = midi.MidiFile()
mf.open(fp)
mf.read()
mf.close()
###

### MIDIUtil Initalizations
MyMIDI = MIDIFile(len(mf.tracks))
volume = 100
tempo = 680
duration = 6   # interval time that key is still pressed
###



prevPitch = -1

mtf = midi.MidiFile()



mt = midi.MidiTrack(len(mf.tracks))
#mtf.tracks = mt


for tracksNum in range (0, len(mf.tracks)):
    
	print 'Track ', tracksNum

	count = 0
	time = count

	MyMIDI.addTempo(tracksNum,time,tempo)

	# Prints out the number of events in a track
	numOfEvents = len(mf.tracks[tracksNum].events)


	
	# Begin reconstruction of the track
	for eventInd in range(0,numOfEvents):

		track = mf.tracks[tracksNum].events[eventInd]
		trackType = track.type

		me = midi.MidiEvent(mt)		
		me.type = trackType


		# event
		event = mf.tracks[tracksNum].events[eventInd]
		eventType = event.type

		if printTracks:
			print event

		pitch = event.pitch
		velocity = event.velocity
		channel = event.channel
		time = event.time
		volume = event.velocity



	        if time is not None:
		    time = track.time
	        else:
		    time = count



		if trackType == 'NOTE_ON':


		    MyMIDI.addNote(tracksNum, channel, pitch, time, duration, volume)

		# Controls instruments
		
		if programChangeOn:		
			if trackType == 'PROGRAM_CHANGE':
			    MyMIDI.addProgramChange(tracksNum, channel, time, event.data)
		
			
		if trackType == 'CONTROLLER_CHANGE':
		    MyMIDI.addControllerEvent(tracksNum, channel, time, event._parameter2, event._parameter1)
		

		prevPitch = event.pitch

		count = count + 1


# Writing reconstructed track
print 'Went through ', len(mf.tracks), ' tracks'

binfile = open("result.mid", 'wb')
MyMIDI.writeFile(binfile)
binfile.close()    
