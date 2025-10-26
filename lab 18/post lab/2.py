import numpy as np 
import matplotlib.pyplot as plt 
from scipy.io import wavfile 
from scipy.signal import correlate 
audio_rate_clean, clean_audio = wavfile.read('clean_audio.wav') 
audio_rate_noisy, noisy_audio = wavfile.read('noisy_audio.wav') 
audio_rate_periodic, periodic_audio = wavfile.read('periodic_audio.wav') 
if not (audio_rate_clean == audio_rate_noisy == audio_rate_periodic): 
raise ValueError("All audio files must have the same sample rate") 
if len(clean_audio.shape) > 1: 
clean_audio = np.mean(clean_audio, axis=1) 
if len(noisy_audio.shape) > 1: 
noisy_audio = np.mean(noisy_audio, axis=1) 
if len(periodic_audio.shape) > 1: 
periodic_audio = np.mean(periodic_audio, axis=1) 
clean_audio = clean_audio / np.max(np.abs(clean_audio)) 
noisy_audio = noisy_audio / np.max(np.abs(noisy_audio)) 
periodic_audio = periodic_audio / np.max(np.abs(periodic_audio)) 
def autocorrelation(x): 
return correlate(x, x, mode='full') / len(x) 
def cross_correlation(x, y): 
return correlate(x, y, mode='full') / min(len(x), len(y)) 
auto_corr_clean = autocorrelation(clean_audio) 
auto_corr_noisy = autocorrelation(noisy_audio) 
auto_corr_periodic = autocorrelation(periodic_audio) 
cross_corr_clean_noisy = cross_correlation(clean_audio, noisy_audio) 
plt.figure(figsize=(12, 10)) 
plt.subplot(4, 1, 1) 
plt.plot(auto_corr_clean, color='b') 
plt.title('Autocorrelation of Clean Audio') 
plt.xlabel('Lag') 
plt.ylabel('Correlation') 
plt.subplot(4, 1, 2) 
plt.plot(auto_corr_noisy, color='g') 
plt.title('Autocorrelation of Noisy Audio') 
plt.xlabel('Lag') 
plt.ylabel('Correlation') 
plt.subplot(4, 1, 3)
plt.plot(auto_corr_periodic, color='r') 
plt.title('Autocorrelation of Periodic Audio') 
plt.xlabel('Lag') 
plt.ylabel('Correlation') 
plt.subplot(4, 1, 4) 
plt.plot(cross_corr_clean_noisy, color='m') 
plt.title('Cross-Correlation between Clean and Noisy Audio') 
plt.xlabel('Lag') 
plt.ylabel('Correlation') 
plt.tight_layout() 
plt.show()

