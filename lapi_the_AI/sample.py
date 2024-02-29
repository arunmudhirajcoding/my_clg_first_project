# import pyaudio
# # import numpy as np
# # import noisereduce as nr
# # import sounddevice as sd
# from noisereduce.noisereduce import reduce_noise as nr
# from noisereduce.spectralgate.stationary import SpectralGateStationary as sd
# from streamed_torch_gate import StreamedTorchGate as np
# # import torch

# # Parameters for recording
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
# RATE = 44100
# CHUNK = 1024
# RECORD_SECONDS = 5
# DEVICE_INDEX = None  # Change this to the index of your microphone device

# Function to record audio
# def record_audio():
#     audio = pyaudio.PyAudio()
#     stream = audio.open(format=FORMAT, channels=CHANNELS,
#                         rate=RATE, input=True,
#                         frames_per_buffer=CHUNK,
#                         input_device_index=DEVICE_INDEX)
#     print("Recording...")
#     frames = []
#     for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#         data = stream.read(CHUNK)
#         frames.append(data)
#     print("Finished recording.")
#     stream.stop_stream()
#     stream.close()
#     audio.terminate()
#     return b''.join(frames)

# # Record audio
# raw_audio = record_audio()

# # Convert raw bytes to numpy array
# audio_data = np.frombuffer(raw_audio, dtype=np.int16)

# # Perform noise reduction
# reduced_noise = nr.reduce_noise(y=audio_data, sr=RATE)

# # Play processed audio
# print("Playing processed audio...")
# sd.play(reduced_noise, samplerate=RATE)
# sd.wait()
# print("Playback finished.")
