import pyaudio
from inspect import getsourcefile
import os.path
import sys
import threading
import numpy as np
import time

""" current_path = os.path.abspath(getsourcefile(lambda:0))
current_dir = os.path.dirname(current_path)
parent_dir = current_dir[:current_dir.rfind(os.path.sep)]

sys.path.insert(0, parent_dir) """

kilThread = False
isthread = False
rate = 44100
bufL=2 #seconds

audBuffer = np.empty(44100)*2

def audthread(devinfo):
    global kilThread 
    global isthread 
    global killed 
    if isthread == False:
        t1 = threading.Thread(target=chldo, args=(devinfo,))
        t1.start()
        isthread = True
    else:
        kilThread = True
        time.sleep(0.3)
        kilThread = False
        print("Changed")
        t1 = threading.Thread(target=chldo, args=(devinfo,))
        t1.start()

def chldo(devinfo):
    global kilThread 
    global isthread 
    global audBuffer
    global rate
    global bufL
    rate = int(devinfo['defaultSampleRate'])
    index = devinfo['index']
    chunk = int(rate/10)
    bufL=5 #seconds
    audBuffer=np.empty(int(rate*bufL))*2  
    PyAud=pyaudio.PyAudio()
    stream=PyAud.open(format=pyaudio.paInt16,channels=1,rate=rate,input=True,input_device_index=index,frames_per_buffer=chunk)
    while True:
        audBuffer[:-chunk] = audBuffer[chunk:]
        audBuffer[-chunk:] = np.frombuffer(stream.read(chunk),dtype=np.int16)  
        if kilThread == True:
            break             

def kilBoi():
    global kilThread
    kilThread = True