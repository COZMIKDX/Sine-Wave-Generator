import math
from random import sample
from time import sleep
import wave
import struct
import itertools
import sys


frequency = float(440) # Hz
samplerate = float(44100) # number of samples per second.
amplitude = 1.0
max_amplitude = 32767.0

generated_data = []
completed_data = []
seconds = 1

def amplitude_boundary_check(amplitude):
	if amplitude > 1.0:
		amplitude = 1.0
	elif amplitude < 0:
		amplitude = 0
	
	return amplitude

def minimum_boundary_check(value):
	if value <= 0:
		value = 1
	return value

def cli_arguments():
	global frequency
	global samplerate
	global amplitude
	global seconds

	number_of_arguments = len(sys.argv)

	if number_of_arguments == 5:
		frequency = minimum_boundary_check(float(sys.argv[1]))
		samplerate = minimum_boundary_check(float(sys.argv[2]))
		amplitude = amplitude_boundary_check(float(sys.argv[3]))
		seconds = minimum_boundary_check(int(sys.argv[4]))
		print("all args!")
	
	
	

# Generates one second of data assuming samplerate 
def generate_data(frequency=440.0, samplerate=44100.0, amplitude=1.0, max_amplitude=32767.0):
	sample_list = []
	for i in range(int(samplerate)):
		one_cycle_per_sample = 2 * math.pi * i
		# x is frequency
		x_cycles_per_second = one_cycle_per_sample * frequency
		x_cycles_per_44100_samples = x_cycles_per_second * (1/samplerate)

		sample_list.append(amplitude * math.sin(x_cycles_per_44100_samples) * max_amplitude)
	
	return sample_list


def extend_data():
	extended_data = []
	for sample in itertools.chain.from_iterable(itertools.repeat(generated_data, seconds)):
		extended_data.append(sample)
	return extended_data


def make_wav_file(samplerate, input_data):
	w = wave.open("testwave.wav", 'wb')
	w.setnchannels(1)
	w.setsampwidth(2)
	w.setframerate(samplerate)

	for sample in input_data:
		data = struct.pack('<h', int(sample))
		w.writeframes(data)

	w.close()


def make_wav_file2(samplerate, input_data, input_data_2):
	w = wave.open("testwave.wav", 'wb')
	w.setnchannels(1)
	w.setsampwidth(2)
	w.setframerate(samplerate)

	for sample in input_data:
		data = struct.pack('<h', int(sample))
		w.writeframes(data)
	
	for sample in input_data_2:
		data = struct.pack('h', int(sample))
		w.writeframes(data)

	w.close()

#--------------------------------------------------------------------------------


cli_arguments()
generated_data = generate_data(frequency, samplerate, amplitude, max_amplitude)
#completed_data = extend_data()

gendata2 = generate_data(100, 44100, .1, max_amplitude)
#completed_data_2 = extend_data()

completed_data_2 = [(generated_data[i] + gendata2[i]) for i in range(len(gendata2))]


#make_wav_file(samplerate, completed_data)
make_wav_file(samplerate, completed_data_2)
#make_wav_file2(samplerate, completed_data, completed_data_2)

