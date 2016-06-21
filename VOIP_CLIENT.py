#!/usr/bin/env python
import pyaudio
import socket
import sys
import time
import Tkinter as tk

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
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

# Main Functionality
while 1:
     def onKeyPress(event):
        data = stream.read(chunk)
        s.send(data)
        s.recv(size)
        text.insert('end', 'You pressed %s\n' % (event.char, ))

root = tk.Tk()
root.geometry('300x200')
text = tk.Text(root, background='black', foreground='white', font=('Comic Sans MS', 12))
text.pack()
root.bind('<KeyPress>', onKeyPress)
root.mainloop()
s.close()
stream.close()
p.terminate()
