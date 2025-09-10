import numpy as np
import matplotlib.pyplot as plt
fs = 1000 # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False) # Time array for 1 second
f1 = 5 # Frequency of the first signal in Hz
f2 = 10 # Frequency of the second signal in Hz
signal1 = np.sin(2 * np.pi * f1 * t) # First sine wave (5 Hz)
signal2 = np.sin(2 * np.pi * f2 * t) # Second sine wave (10 Hz)
combined_signal = signal1 + signal2
plt.figure(figsize=(10, 8))
plt.subplot(3, 1, 3)
plt.plot(t, combined_signal)
plt.title('Combined Signal (5 Hz + 10 Hz)')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()