import numpy as np
import matplotlib.pyplot as plt
fs = 500 # Sampling frequency in Hz
t = np.linspace(0, 2, 2 * fs, endpoint=False) # Time array for 2 seconds
f = 5 # Frequency of the sine wave in Hz
original_signal = np.sin(2 * np.pi * f * t)
time_shift = 0.1 # Time shift in seconds
shifted_signal = np.sin(2 * np.pi * f * (t - time_shift))
plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original Signal')
plt.plot(t, shifted_signal, label='Shifted Signal (0.1 s delay)', linestyle='--')
plt.title('Original and Shifted 5 Hz Sine Wave Signals')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()