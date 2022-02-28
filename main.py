import time
import hidemsg
import showmsg

def wrongAction ():
    print ("You didn't chose a valid option, closing program")
    time.sleep (1)
    print (".......")
    time.sleep (1)
    print ("Program closed succesfully")
    quit()

def chooseMidiFileHide():
    midiAudio= "Elaudio"
    actionMidi = input ("Choose a file to hide message in: \n[1] Default: 'Mary.midi' \n"
    + "[2] Personal choice \n")
    if actionMidi == "1":
        midiAudio ="Mary.mid"
    elif actionMidi == "2":
        customName = input ("Input the midi files name \n")
        if not customName.endswith(".mid"):
            print ("file must be a .mid")
            wrongAction()

        midiAudio = customName
    else:
        wrongAction()
    print (midiAudio)
    return midiAudio


action = input ("What do you want to do?"+ "\n"+ "[1] Hide Message \n[2] Expose Message \n")

if action == "1":
    msg = input ("Please type the msg to hide: \n")
    if len(msg) >0:
        print ('The message you are trying to hide is: "'+msg+'"')
        midiAudio = chooseMidiFileHide()
        hidemsg.hideMsg(midiAudio, msg)
    else:
        wrongAction()
elif action == "2":
    exposeAct = input( "Please choose the Midi file containing the hidden message"+
    "\n[1] Default Midi File \n[2] Custome Midi File \n")
    if exposeAct == "1":
        showmsg.exposeMsg("Audio_with_Hidden_Msg.mid")
    elif exposeAct == "2":
        customName = input ("Input the midi files name \n")
        if not customName.endswith(".mid"):
            print ("file must be a .mid")
            wrongAction()
        else:
            try:
                showmsg.exposeMsg(customName)
            except:
                print ("File not found, make sure the Midi file is in this directory")

            
else:
    wrongAction()
