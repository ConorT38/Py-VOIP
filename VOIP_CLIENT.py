import pyaudio
import socket
import sys
import time
import threading
from Tkinter import *

# Pyaudio Initialization
chunk = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 10240

p = pyaudio.PyAudio()

stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)

# Socket Initialization
host = 'localhost'
port = 50000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect((host,port))

class VOIP_FRAME(Frame):
    
    def OnMouseDown(self, event):
        self.mute = False
        self.speakStart()
        
    def muteSpeak(self,event):
        self.mute = True
        print("You are now muted")
        
    def speakStart(self):
        t = threading.Thread(target=self.speak)
        t.start()
                
    def speak(self):
        print("You are now speaking")
        while self.mute is False:
            data = stream.read(chunk)
            s.send(data)
            s.recv(size)
        

    def createWidgets(self):
        self.speakb = Button(self)
        self.speakb["text"] = "Speak"
        self.speakb.pack({"side": "left"})

        self.speakb.bind("<ButtonPress-1>", self.OnMouseDown)
        self.speakb.bind("<ButtonRelease-1>", self.muteSpeak)

    def __init__(self, master=None):
        self.mute = True
        Frame.__init__(self, master)
        self.mouse_pressed = False
        self.pack()
        self.createWidgets()

root = Tk()
app = VOIP_FRAME(master=root)
app.mainloop()
root.destroy()
s.close()
stream.close()
p.terminate()

    
