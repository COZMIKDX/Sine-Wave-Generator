# Simple Sine Wave Generator
This generates sine waves given a desired frequency, samplerate, amplitude, and duration in seconds (as integers).

## Usage
Arguments for this script are frequency, samplerate, amplitude, and seconds.
Seconds is an integer value. The rest are floats.
Amplitude can be a value from 0 to 1.
No arguments provided will result in a wave where frequency = 440, samplerate = 44100, amplitude = 1, and seconds = 1.

### Example:
```
python3 sintest.py 100 44100 1 3
```
This would generate a sine wave with a frequency of 100 Hz. 44100 samples would be taken to create one second worth of data.
Then that data would be copied to provide as much data as needed to produce 3 seconds.

Lastly, writing the data to a wave file currently takes the longest.
This is more noticeable once you try to make more than a few seconds of data.

## To Do
- make a way to name the output file
- maybe make a gui
- it can combine multiple waves but needs a way to do that without editing the code

## Some notes I took while making this.
 "sample" here would be the x-value on a graph. 1000 samples would be from x=0 to x=1000.
 A "second" is represented on the same graph as some amount of samples.
 A regular sin(x) would complete one cycle in 2pi samples (about every x=2pi=6.238 on a graph).

 sin(2pi * x) would be 2pi cycles within 2pi samples. That means about 6.238 whole cycles from
 x=0 to x=2pi=6.238. We can simplify this: 2pi cycles / 2pi samples = 1 cycle / 1 sample.

 sin(1000 * 2pi * x): If we multiply the argument by our desired frequency, say 1000, we would then be getting 1000 cycles.
 This would be per one sample still since this would only multiply the numerator.
 So, if we graphed sin(3 * 2pi * x), we would see about 3 complete cycles between x=0 and x=1.
 Here, we could say one sample = one second. That way we'd have 1000 cycles per second.
 We used seconds here because this helps later with involving sample rate, which is samples per second.

 sin(1000 * 2pi * x * 1/44100) Finally, involving sample rate. Say we want 44100 samples per second. 
 So, we want 44100 samples of those 1000 cycles every second. Since those 1000 cycles occur in one second,
 This lines up nicely.
 Note: After this the units are now cycles/sample.
 On a graph this would look pretty stretched out compared to the previous functions.
 1000 cycles / 44100 samples == 1 cycle / 44.1 samples. So there would be one complete cycle
   from x=0 to x=44.1.
 Note: Our sample rate is 44100 samples / second, so 44100 samples (x-values) make up one second.
 That's why the graph would look stretched out, because we redefined how many x-values correspond
 to one second.
