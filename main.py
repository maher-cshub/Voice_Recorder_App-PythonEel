
import sounddevice
from scipy.io.wavfile import write
import eel






# name of folder where the html, css, js, image files are located
eel.init('templates')

@eel.expose
def Record(name):
    fs=44100 #sample_rate
    print("Recording....\n")
    while True:
        record_voice=sounddevice.rec(frames=fs,channels=2)
        sounddevice.wait()
        result = eel.Check_Recording()()
        print(result)
        if (result):
            break
    Save(name,record_voice,fs)
        



@eel.expose
def Save(name,audio,fs):
        write(f"{name}.wav",fs,audio)
        print("Finished...\nPlease Check it...")
        return

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))



