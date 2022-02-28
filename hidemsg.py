from re import M
import sys
import midi

def msgToASCII (msg):
    return [ord(m) for m in msg]

def hideMsg(audio, msg):
    chars= msgToASCII(msg)
    midiFile = midi.read_midifile(audio)

    for track in midiFile:
        for event in track:
            if isinstance(event, midi.events.ProgramChangeEvent):
                current = event

                for char in chars:
                    track.append(midi.ProgramChangeEvent(tick = 0, channel = 1, data = [char]))
                track.append(current)
                midi.write_midifile("Audio_with_Hidden_Msg.mid", midiFile) 
                return 

