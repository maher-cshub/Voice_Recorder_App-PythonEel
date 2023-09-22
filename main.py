
import sounddevice
import pyaudio
from scipy.io.wavfile import write
import eel


# name of folder where the html, css, js, image files are located
eel.init('templates')



class Recorder():


    def __init__(self):
        self.rec1 = pyaudio.PyAudio()
        self.input_devices = self.get_input_device()

    def get_input_device(self):
        total_devices = self.rec1.get_host_api_count()
        devices = {}
        for i in range(total_devices):
            devices[i] = self.rec1.get_device_info_by_index(i)['name']
        return devices


@eel.expose
def Record(name):
    recorder = Recorder()
    eel.Set_Mics(recorder.input_devices)()
    return
    fs=44100 #sample_rate
    print("*********Recording****************\n")
    while True:
        record_voice=sounddevice.rec(frames=fs,channels=2)
        sounddevice.wait()
        result = eel.Check_Recording()()
        if (result == "false"):
            break
    Save(name,record_voice,fs)
        



@eel.expose
def Save(name,audio,fs):
        write(f"{name}.mp3",fs,audio)
        print("Finished...\nPlease Check it...")
        return

@eel.expose
def Resume(name,audio,fs):
     return
     

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))



