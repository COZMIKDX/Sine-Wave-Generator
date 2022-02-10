import math
from random import sample
from time import sleep
import wave
import struct
import itertools

frequency = float(440) # Hz
samplerate = float(44100) # number of samples per second.
amplitude = 1.0


generated_data = []
completed_data = []
seconds = 10
def generate_data(frequency=440.0, samplerate=44100.0, amplitude=1.0, max_amplitude=32767.0):
	sample_list = []
	for i in range(int(samplerate)):
		one_cycle_per_sample = 2 * math.pi * i
		# x is frequency
		x_cycles_per_second = one_cycle_per_sample * frequency
		x_cycles_per_44100_samples = x_cycles_per_second * (1/samplerate)

		sample_list.append(amplitude * math.sin(x_cycles_per_44100_samples) * 32767.0)
	
	return sample_list
	
generated_data = generate_data()

w = wave.open("testwave.wav", 'wb')
w.setnchannels(2)
w.setsampwidth(2)
w.setframerate(samplerate)

max_amplitude = 32767.0 # 16-bit range is -32767 to 32767

for sample in itertools.chain.from_iterable(itertools.repeat(generated_data, seconds * 2)):
	completed_data.append(sample)

print(len(generated_data))
print(len(completed_data))

for sample in completed_data:
	data = struct.pack('<h', sample)
	w.writeframes(data)


w.close()
