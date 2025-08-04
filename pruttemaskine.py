import sounddevice as sd
import soundfile as sf
import random

def select_random_sound(sounds):
    sound = random.choice(sounds)
    return sound

def play_sound(filename):
    # Extract data and sampling rate from file
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing
    return {'message': f'Played {filename}'}
