
# Experiment 6: Design FIR Filter using Windowing Method
# FIR Low-Pass Filter using Hann Window

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz

# Main Code: FIR Low-Pass Filter
Fs = 10000
Fc = 3000
N = 31

b = firwin(
    numtaps=N,
    cutoff=Fc,
    window='hann',
    pass_zero='lowpass',
    fs=Fs
)

f, H = freqz(b, worN=2048, fs=Fs)
magnitude_db = 20 * np.log10(np.maximum(np.abs(H), 1e-10))

plt.figure(figsize=(10, 5))
plt.plot(f, magnitude_db)
plt.title('FIR Low-Pass Filter using Hann Window')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.tight_layout()
plt.show()

print("FIR Filter Coefficients:")
print(b)


# 1. FIR Low-Pass Filter
b = firwin(N, 3000, window='hann', pass_zero='lowpass', fs=Fs)
f, H = freqz(b, worN=2048, fs=Fs)
plt.plot(f, 20 * np.log10(np.maximum(np.abs(H), 1e-10)))
plt.title('FIR Low-Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.show()


# 2. FIR High-Pass Filter
b = firwin(N, 3000, window='hann', pass_zero='highpass', fs=Fs)
f, H = freqz(b, worN=2048, fs=Fs)
plt.plot(f, 20 * np.log10(np.maximum(np.abs(H), 1e-10)))
plt.title('FIR High-Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.show()


# 3. FIR Band-Pass Filter
b = firwin(N, [3000, 4000], window='hann',
           pass_zero='bandpass', fs=Fs)
f, H = freqz(b, worN=2048, fs=Fs)
plt.plot(f, 20 * np.log10(np.maximum(np.abs(H), 1e-10)))
plt.title('FIR Band-Pass Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.show()


# 4. FIR Band-Stop Filter
b = firwin(N, [3000, 4000], window='hann',
           pass_zero='bandstop', fs=Fs)
f, H = freqz(b, worN=2048, fs=Fs)
plt.plot(f, 20 * np.log10(np.maximum(np.abs(H), 1e-10)))
plt.title('FIR Band-Stop Filter')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
plt.show()
