from re import I
import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fft import fft
import numpy as np

# sampleTime = 50
plotHzLow = 899.1         
plotHzHigh = 899.8
# plt.rcParams['agg.path.chunksize'] = 100000
# file = 'w8rko30m.wav'
# startSeconds = 50

# file = 'w8rko40m.wav'
# startSeconds = 2 * 60 + 50
startSeconds = 0

# file = 'w8rko80m.wav'
# startSeconds = 2 * 60 + 20
# startSeconds = 0

# file = 'k5cm30m.wav'
# startSeconds = 4 * 60 + 55

file = 'WWV10_15.wav'

rate, data0 = wav.read(file)
startSample = (startSeconds * rate)
sampleCount = len(data0) - startSample
# sampleCount = 120 * rate
# print ("SampleCount = %d" % sampleCount)
data = list(map(lambda x: x[0], data0[startSample: startSample + sampleCount]))
fft_out = fft(data)
startPlotData = int(sampleCount / rate * plotHzLow)
numSamplesToPlot = int(sampleCount / rate * (plotHzHigh - plotHzLow))
a0 = np.abs(fft_out)[startPlotData:startPlotData + numSamplesToPlot]
data = list(map(lambda x: x[1], data0[startSample: startSample + sampleCount]))
fft_out = fft(data)
startPlotData = int(sampleCount / rate * plotHzLow)
numSamplesToPlot = int(sampleCount / rate * (plotHzHigh - plotHzLow))
a1 = np.abs(fft_out)[startPlotData:startPlotData + numSamplesToPlot]
max_y = 0
max_y_x = 0
i = 0
for y in a0[:int(numSamplesToPlot)]:
    if y > max_y:
        max_y = y
        max_y_x = i 
    i += 1

peak0_x = max_y_x

max_y = 0
max_y_x = 0
i = 0
for y in a1[:int(numSamplesToPlot)]:
    if y > max_y:
        max_y = y
        max_y_x = i 
    i += 1

peak1_x = max_y_x


# max_y = 0
# max_y_x = 0
# i = 0
# for y in a[peak1_x + 1000:int(numSamplesToPlot / 2)]:  # LSB
# # for y in a[int(peak1_x - 100):]: # USB
#     if y > max_y:
#         max_y = y
#         max_y_x = i 
#     i += 1

# peak2_x = max_y_x

# print (len(fft_out))
b = list(map(lambda x: x * rate / sampleCount + plotHzLow, range(0,numSamplesToPlot)))
plt.plot(b, a0)
plt.plot(b, a1)
plt.title('FMT %s\nPeak Frequency: %0.2f %0.2f Hz' % (file, peak0_x * rate / sampleCount + plotHzLow, peak1_x * rate / sampleCount + plotHzLow))
plt.xlabel('Frequency (Hz)')
plt.show()
