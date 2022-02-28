import midi

def msgToASCII (evtMsg):
	msg =  [chr(event.data[0]) for event in evtMsg]
	msg = msg[:-1]
	return ''.join(msg)

def exposeMsg (audio):
    midiFile = midi.read_midifile(audio)
    eventsList = []

    for track in midiFile:
        for event in track:
            if isinstance (event, midi.events.ProgramChangeEvent):
                eventsList.append(event)
        
    if len(eventsList) > 1:
        print (msgToASCII(eventsList))
    else:
        print ("No message found")
        quit()
