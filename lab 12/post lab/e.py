import numpy as np
import matplotlib.pyplot as plt
fs = 500 # Sampling frequency in Hz
t = np.linspace(0, 1, fs, endpoint=False) # Time array for 1 second
f = 5 # Frequency of the sine wave in Hz
original_signal = np.sin(2 * np.pi * f * t)
reversed_signal = original_signal[::-1] # Reverse the array
plt.figure(figsize=(10, 6))
plt.plot(t, original_signal, label='Original Signal')
plt.plot(t, reversed_signal, label='Reversed Signal', linestyle='--')
plt.title('Original and Reversed 5 Hz Sine Wave Signals')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()