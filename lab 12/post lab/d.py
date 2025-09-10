import numpy as np
import matplotlib.pyplot as plt
fs = 500
t = np.linspace(0, 1, fs, endpoint=False)
f = 10
original_signal = np.sin(2 * np.pi * f * t)
scaled_signal = 3 * original_signal
plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original Signal')
plt.plot(t, scaled_signal, label='Scaled Signal (Amplitude * 3)', linestyle='--')
plt.title('Original and Scaled 10 Hz Sine Wave Signals')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()