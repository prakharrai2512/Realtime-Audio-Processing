import pyaudio

p = pyaudio.PyAudio()
info = p.get_host_api_info_by_index(0)
numdevices = info.get('deviceCount')

def retlist():
        aud_list={}
        for i in range (0,numdevices):
                if p.get_device_info_by_host_api_device_index(0,i).get('maxInputChannels')>0:
                        devinfo = p.get_device_info_by_index(i)
                        aud_list.update({i:devinfo})
        return aud_list


