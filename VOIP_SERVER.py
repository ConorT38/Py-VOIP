#!/usr/bin/env python
import pyaudio
import socket
import sys

# Pyaudio Initialization
chunk = 1024
pa = pyaudio.PyAudio()

# Opening of the audio stream
stream = pa.open(format = pyaudio.paInt16,
                channels = 1,
                rate = 10240,
                output = True)

# Socket Initialization
host = 'localhost'
port = 50000
backlog = 5
size = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(backlog)

client, address = sock.accept()
print "Server is now running\n======================="

# Main Functionality
while 1:
    data = client.recv(size)
    if data:
        # Write data to pyaudio stream
        stream.write(data)  # Stream the recieved audio data
        client.send('ACK')  # Send an ACK

client.close()
stream.close()
pa.terminate()
print "Server has stopped running"
