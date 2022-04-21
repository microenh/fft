from re import I
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fft import fft
import numpy as np

file = 'ic7610.wav'
plotHzLow = 999         
plotHzHigh = 1001
startSeconds = 0

rate, data = wav.read(file)
startSample = (startSeconds * rate)
sampleCount = len(data) - startSample
fft_out = fft(data)
startPlotData = int(sampleCount / rate * plotHzLow)
numSamplesToPlot = int(sampleCount / rate * (plotHzHigh - plotHzLow))
a0 = np.abs(fft_out)[startPlotData:startPlotData + numSamplesToPlot]
max_y = 0
max_y_x = 0
i = 0
for y in a0[:int(numSamplesToPlot)]:
    if y > max_y:
        max_y = y
        max_y_x = i 
    i += 1

peak0_x = max_y_x

b = list(map(lambda x: x * rate / sampleCount + plotHzLow, range(0,numSamplesToPlot)))
plt.plot(b, a0)
plt.title('FMT %s\nPeak Frequency: %0.2f Hz' % (file, peak0_x * rate / sampleCount + plotHzLow,))
plt.xlabel('Frequency (Hz)')
plt.show()
