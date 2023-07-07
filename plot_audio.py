import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, rfft, rfftfreq
from pydub import AudioSegment

dzwiek = AudioSegment.from_wav("resources/lethergo.wav")
channels = dzwiek.split_to_mono()
channel1 = channels[0]
channel2 = channels[1]
channel1.export("resources/channel1.wav", format="wav")
channel2.export("resources/channel2.wav", format="wav")


obj1 = wave.open("resources/channel1.wav", "rb")
obj2 = wave.open("resources/channel2.wav", "rb")

def plt_time(audiofile):

    sample_freq = audiofile.getframerate()
    n_samples = audiofile.getnframes()
    signal_wave = audiofile.readframes(-1)

    audiofile.close()

    t_audio = n_samples/sample_freq

    signal_array = np.frombuffer(signal_wave, dtype=np.int16)

    times = np.linspace(0,t_audio, num=n_samples)

    plt.figure(figsize=(15,5))
    plt.plot(times,signal_array)
    plt.title("Audio signal")
    plt.ylabel("Signal wave")
    plt.xlabel("Time [s]")
    plt.xlim(0,t_audio)
    plt.show()

def plt_fft(audiofile):
    signal_wave = audiofile.readframes(-1)
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)
    N = len(signal_array)
    normalize = N / 2
    sampling_rate = audiofile.getframerate()
    frequency_axis = rfftfreq(N,d=1.0/sampling_rate)
    norm_amplitude = np.abs(rfft(signal_array))/normalize

    plt.figure(figsize=(15, 5))
    plt.plot(frequency_axis,norm_amplitude)
    plt.title("FFT")
    plt.ylabel("Amplitude")
    plt.xlabel("Frequency [Hz]")
    plt.show()
    #cmath fft na real channel1 imag channel2



if __name__ == "__main__":
    # plt_time(obj2)
    # plt_time(obj2)
    #
    plt_fft(obj1)