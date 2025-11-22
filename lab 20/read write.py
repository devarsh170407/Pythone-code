import soundfile as sf
# Load audio file
audio, sample_rate = sf.read(r'C:\Users\devar\Downloads\download.MP3')

# Write audio file
sf.write('new_audio_file.wav', audio, sample_rate)
