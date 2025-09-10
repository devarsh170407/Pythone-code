import numpy as np 
import matplotlib.pyplot as plt 
fs = 500 # Sampling frequency in Hz 
t = np.linspace(0, 2, 2 * fs, endpoint=False) # Time array for 2 seconds 
f1 = 5 # Frequency of the sine wave in Hz 
sine_wave = np.sin(2 * np.pi * f1 * t) 
f2 = 10 # Frequency of the cosine wave in Hz 
cosine_wave = np.cos(2 * np.pi * f2 * t) 
resulting_signal = sine_wave * cosine_wave 
plt.figure(figsize=(10, 8)) 
plt.subplot(3, 1, 3) 
plt.plot(t, resulting_signal) 
plt.title('Resulting Signal (5 Hz Sine Wave * 10 Hz Cosine Wave)') 
plt.xlabel('Time [s]') 
plt.ylabel('Amplitude') 
plt.tight_layout() 
plt.show()
