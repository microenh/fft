import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
rate, data = wav.read('w8rko30m.wav')
data = list(map(lambda x: x[1], data))
plt.plot(data[48000:49000])
plt.show()