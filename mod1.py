import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
plt.rcParams['agg.path.chunksize'] = 1000
rate, data = wav.read('w8rko30m.wav')
# data = list(map(lambda x: x[0], data))
fft_out = fft(data)
plt.plot(data, np.abs(fft_out))
# plt.plot(range(len(data)), np.abs(fft_out))
plt.show()