
import wave
import pyaudio
from scipy.io.wavfile import write
import eel
import time


# name of folder where the html, css, js, image files are located
eel.init('templates')



class Recorder():

    def __init__(self):
        self.recorder = pyaudio.PyAudio()
        self.input_devices = self.get_input_device()
        self.mic_select = ""
        self.file_name = ""
        self.stream_audio = ""
        self.audio_data = []
        self.data = ""

    def get_input_device(self):
        total_devices = self.recorder.get_host_api_count()
        devices = {}
        for i in range(total_devices):
            devices[i] = self.recorder.get_device_info_by_index(i)['name']
        return devices
    
    def record(self,status):
        
        if (status == "inactive"):
            new_state = eel.Change_Status("recording")()
            self.stream_audio = self.recorder.open(input=True,input_device_index=int(self.mic_select),rate=44000,channels=10,format=pyaudio.paInt16,frames_per_buffer=1024)
            self.stream_audio.start_stream()
            while new_state == "recording":
                self.data = self.stream_audio.read(1024)
                self.audio_data.append(self.data)
                new_state = eel.Check_Status()()
            
        elif(status == "recording"):
            if (self.stream_audio.is_active):
                self.stream_audio.stop_stream()
                self.stream_audio.close()
            eel.Change_Status("inactive")()
            
    
    def save(self):
         self.recorder.terminate()
         sound_file = wave.open(self.file_name+".wav","wb")
         sound_file.setnchannels(10)
         sound_file.setsampwidth(self.recorder.get_sample_size(pyaudio.paInt16))
         sound_file.setframerate(44000)
         sound_file.writeframes(b"".join(self.audio_data))

rec = Recorder()

@eel.expose
def Start():
    eel.Set_Mics(rec.input_devices)()

@eel.expose
def Set_Vars(file_name,mic_select):
    rec.file_name = file_name
    rec.mic_select = mic_select

@eel.expose
def Record(status):
    rec.record(status)

        
@eel.expose
def Save():
    rec.save()

@eel.expose
def Resume(name,audio,fs):
     return
     

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))



