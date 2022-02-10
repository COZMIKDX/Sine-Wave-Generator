import math
from random import sample
from time import sleep
import wave
import struct
import itertools

frequency = float(440) # Hz
samplerate = float(44100) # number of samples per second.
amplitude = 1
period = float(samplerate) / float(frequency)

# returns what part of the period in the wave to calculate.
def period_cycle(i):
	return i % float(period)

sample_list = []
full_data_list = []
seconds = 10
for i in range(int(samplerate)):
	one_cycle_per_sample = 2 * math.pi * i
	# x is frequency
	x_cycles_per_second = one_cycle_per_sample * frequency
	x_cycles_per_44100_samples = x_cycles_per_second * (1/samplerate)

	sample_list.append(amplitude * math.sin(x_cycles_per_44100_samples) * 32767.0)
	

w = wave.open("testwave.wav", 'wb')
w.setnchannels(2)
w.setsampwidth(2)
w.setframerate(samplerate)

max_amplitude = 32767.0 # 16-bit range is -32767 to 32767

#sample_list2 = []
#for sample in sample_list:
#	sample_list2.append(int(sample * max_amplitude))

#for sample in itertools.chain.from_iterable(itertools.repeat(sample_list2, seconds * 2)):
#	full_data_list.append(sample)

for sample in itertools.chain.from_iterable(itertools.repeat(sample_list, seconds * 2)):
	full_data_list.append(sample)

print(len(sample_list))
print(len(full_data_list))

for sample in full_data_list:
	data = struct.pack('<h', sample)
	#w.writeframesraw(data)
	#packed_data.append(struct.pack('h', sample))
	w.writeframes(data)


w.close()
