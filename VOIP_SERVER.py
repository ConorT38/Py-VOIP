#!/usr/bin/env python
import pyaudio
import socket
import sys

# Pyaudio Initialization
chunk = 1024
p = pyaudio.PyAudio()

stream = p.open(format = pyaudio.paInt16,
                channels = 1,
                rate = 10240,
                output = True)

# Socket Initialization
host = 'localhost'
port = 50000
backlog = 5
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(backlog)

client, address = s.accept()

# Main Functionality
while 1:
    data = client.recv(size)
    if data:
        # Write data to pyaudio stream
        stream.write(data)  # Stream the recieved audio data
        client.send('ACK')  # Send an ACK

client.close()
stream.close()
p.terminate()
