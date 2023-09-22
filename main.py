
import wave
import pyaudio
from scipy.io.wavfile import write
import eel
import time


# name of folder where the html, css, js, image files are located
eel.init('templates')


class Recorder():

    def __init__(self):
        self.recorder = ""
        self.input_devices = self.get_input_device()
        self.mic_select = ""
        self.file_name = ""
        self.stream_audio = ""
        self.audio_data = []
        self.data = ""

    def get_input_device(self):
        p_audio = pyaudio.PyAudio()
        total_devices = p_audio.get_host_api_count()
        devices = {}
        for i in range(total_devices):
            devices[i] = p_audio.get_device_info_by_index(i)['name']
        p_audio.terminate()
        return devices
    
    def record(self,status):      
        if (status == "inactive"):
            self.recorder = pyaudio.PyAudio()
            self.listen()
            
        elif(status == "recording"):
            self.pause()

        elif(status == "paused"):
            self.listen()

    def listen(self):
        new_state = eel.Change_Status("recording")()
        self.stream_audio = self.recorder.open(input=True,input_device_index=int(self.mic_select),rate=44000,channels=10,format=pyaudio.paInt16,frames_per_buffer=1024)
        while new_state == "recording":
            self.data = self.stream_audio.read(1024)
            self.audio_data.append(self.data)
            new_state = eel.Check_Status()()
            
    def pause(self):
        eel.Change_Status("paused")()
        self.stream_audio.stop_stream()
        self.stream_audio.close()
        
    
    def save(self):
         self.recorder.terminate()
         sound_file = wave.open(self.file_name+".wav","wb")
         sound_file.setnchannels(10)
         sound_file.setsampwidth(self.recorder.get_sample_size(pyaudio.paInt16))
         sound_file.setframerate(44000)
         sound_file.writeframes(b"".join(self.audio_data))
         eel.Change_Status("inactive")()

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

# 1000 is width of window and 600 is the height
eel.start('index.html', size=(1000, 600))



