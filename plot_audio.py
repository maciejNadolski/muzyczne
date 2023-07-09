import wave
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import fft, fftfreq, rfft, rfftfreq
from pydub import AudioSegment
import math

class spectrumAnalysis:

    def convert_stereo(file,nazwaL,nazwaR):
        dzwiek = AudioSegment.from_wav(file)
        channels = dzwiek.split_to_mono()
        channel1 = channels[0]
        channel2 = channels[1]
        channel1.export("/resources/"+nazwaL, format="wav")
        channel2.export("/resources/"+nazwaR, format="wav")
        print("Wyeksportowano do /resources")




    obj1 = wave.open("resources/channel1.wav", "rb")
    obj2 = wave.open("resources/channel2.wav", "rb")

    def plt_time(audiofile):
        sample_freq = audiofile.getframerate()
        n_samples = audiofile.getnframes()
        signal_wave = audiofile.readframes(-1)

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

    def plt_fft_mono(audiofile):

        signal_wave = audiofile.readframes(-1)
        signal_array = np.frombuffer(signal_wave, dtype=np.int16)
        N = len(signal_array)
        normalize = N / 2

        sampling_rate = audiofile.getframerate()
        frequency_axis = rfftfreq(N,d=1.0/sampling_rate)
        norm_amplitude = np.abs(rfft(signal_array))/normalize

        decibels = 10 * np.log10(norm_amplitude / 1)

        plt.figure(figsize=(15, 5))
        plt.plot(frequency_axis,decibels)
        plt.title("FFT")
        plt.ylabel("Amplitude")
        plt.xlabel("Frequency [Hz]")
        plt.show()


    def plt_fft_stereo(audiofile1, audiofile2):
        #oba kanały powinny miec tą samą częstotliwość, zrobić try catch  na to lub assert w przyszłości
        signal_wave1 = audiofile1.readframes(-1)
        signal_wave2 = audiofile2.readframes(-1)
        signal_array1 = np.frombuffer(signal_wave1, dtype=np.int16)
        signal_array2 = np.frombuffer(signal_wave2, dtype=np.int16)

        fun = signal_array1 + signal_array2*1j
        N = len(signal_array1)

        sampling_rate = audiofile1.getframerate()

        normalize = N / 2
        frequency_axis = fftfreq(N, d=1.0 / sampling_rate)
        norm_amplitude = np.abs(fft(fun)) / normalize
        decibels = 10 * np.log10(norm_amplitude/1)

        plt.figure(figsize=(15, 5))
        plt.plot(frequency_axis, decibels)
        plt.xlim(0,25000)
        plt.title("FFT")
        plt.ylabel("Intensivity [dB]")
        plt.xlabel("Frequency [Hz]")
        plt.show()




if __name__ == "__main__":
    test1 = spectrumAnalysis
    obj1 = wave.open("resources/channel1.wav", "rb")
    obj2 = wave.open("resources/channel2.wav", "rb")
    test1.plt_fft_stereo(obj1,obj2)
    obj1.close()
    obj2.close()
