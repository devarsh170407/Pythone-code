import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 
from scipy.signal import fftconvolve, convolve 
audio_rate, audio_data = wavfile.read('audio_file.wav') 
impulse_rate, impulse_response = wavfile.read('impulse_response.wav') 
if audio_rate != impulse_rate: 
raise ValueError("Audio file and impulse response must have the same sample rate") 
if len(audio_data.shape) > 1: 
audio_data = np.mean(audio_data, axis=1) 
if len(impulse_response.shape) > 1: 
impulse_response = np.mean(impulse_response, axis=1) 
audio_data = audio_data / np.max(np.abs(audio_data)) 
impulse_response = impulse_response / np.max(np.abs(impulse_response)) 
linear_conv = convolve(audio_data, impulse_response, mode='full') 
n = len(audio_data)
m = len(impulse_response) 
circular_conv = np.fft.ifft(np.fft.fft(audio_data, n+m-1) * np.fft.fft(impulse_response, n+m-1)).real 
plt.figure(figsize=(12, 8)) 
plt.subplot(3, 1, 1) 
plt.plot(audio_data, color='b') 
plt.title('Original Audio') 
plt.xlabel('Sample') 
plt.ylabel('Amplitude') 
plt.subplot(3, 1, 2) 
plt.plot(linear_conv, color='g') 
plt.title('Linear Convolution Result') 
plt.xlabel('Sample') 
plt.ylabel('Amplitude') 
plt.subplot(3, 1, 3) 
plt.plot(circular_conv, color='r') 
plt.title('Circular Convolution Result') 
plt.xlabel('Sample') 
plt.ylabel('Amplitude') 
plt.tight_layout() 
plt.show()
