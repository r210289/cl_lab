import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
amplitude = 1
frequency = 2  # in Hz
duration = 1  # in seconds
sampling_rate = 1000  # in samples per second

# Generate the time vector
t = np.arange(0, duration, 1 / sampling_rate)

# Generate the sine wave
sin_wave = amplitude * np.sin(2 * np.pi * frequency * t)

# Plot the sine wave
plt.plot(t, sin_wave)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Sine Wave')
plt.grid(True)
plt.show()

