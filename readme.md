# "sample" here would be x-value a graph. 1000 samples would be from x=0 to x=1000.
	# A "second" is represented on the same graph as some amount of samples.

	# A regular sin(x) would complete one cycle in 2pi samples (about every x=2pi=6.238 on a graph).

	# sin(2pi * x) would be 2pi cycles within 2pi samples. That means about 6.238 whole cycles from
	# x=0 to x=2pi=6.238. We can simplify this: 2pi cycles / 2pi samples = 1 cycle / 1 sample.

	# sin(1000 * 2pi * x): If we multiply the argument by our desired frequency, say 1000, we would then be getting 1000 cycles.
	# This would be per one sample still since this would only multiply the numerator.
	# So, if we graphed sin(3 * 2pi * x), we would see about 3 complete cycles between x=0 and x=1.
	# Here, we could say one sample = one second. That way we'd have 1000 cycles per second.
	# We used seconds here because this helps later with involving sample rate, which is samples per second.

	# sin(1000 * 2pi * x * 1/44100) Finally, involving sample rate. Say we want 44100 samples per second. 
	# So, we want 44100 samples of those 1000 cycles every second. Since those 1000 cycles occur in one second,
	# This lines up nicely.
	# Note: After this the units are now cycles/sample.
	# On a graph this would look pretty stretched out compared to the previous functions.
	# 1000 cycles / 44100 samples == 1 cycle / 44.1 samples. So there would be one complete cycle
	#   from x=0 to x=44.1.
	# Note: Our sample rate is 44100 samples / second, so 44100 samples (x-values) make up one second.
	# That's why the graph would look stretched out, because we redefined how many x-values correspond
	# to one second.