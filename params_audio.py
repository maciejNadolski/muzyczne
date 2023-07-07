# Audio files
# .mp3 - kompresja, duże straty
# .flac - kompresja, mniejsze straty
# .wav - brak kompresji, brak strat


# Audio parameters:
# - liczba kanałów (1 mono, 2 stereo)
# - liczba bajtów na próbkę
# - częstość próbkowania : często 44100 Hz
# - liczba klatek
# - wartość klatki


import wave

obj = wave.open("resources/lethergo.wav", "rb") #odczytaj binarnie

print("Numbers of channels: ", obj.getnchannels())
print("sample width:", obj.getsampwidth())
print("frame rate:", obj.getframerate())
print("Number of frames:", obj.getnframes())
print("parameters:", obj.getparams())

t_audio = obj.getnframes()/obj.getframerate()    #czas w sekundach
print(t_audio)

frames = obj.readframes(-1) #czyta wszystkie framey
print(type(frames), type(frames[0]))
print(len(frames)/4)

obj.close()

obj_new = wave.open("resources/lethergo_new2.wav","wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(44100.0)
obj_new.writeframes(frames)

obj_new.close()