'''
Created on Jan 27, 2020

@author: goyalpushkar
'''

if __name__ == '__main__':
    pass

import scipy.io.wavfile as wavFile
import numpy

contents = wavFile.read("")
samplerate = contents[0]
data = contents[1].tolist()

wavFile.write("output.wav", samplerate, numpy.asarray(data, dtype="int16"))
