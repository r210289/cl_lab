import numpy as np
import matplotlib.pyplot as plt

# Define the parameters for the first sine wave
amplitude1 = 1
frequency1 = 2  # in Hz

# Define the parameters for the second sine wave
amplitude2 = 0.5
frequency2 = 3  # in Hz

# Define the common parameters
duration = 1  # in seconds
sampling_rate = 1000  # in samples per second

# Generate the time vector
t = np.arange(0, duration, 1 / sampling_rate)

# Generate the sine waves
sin_wave1 = amplitude1 * np.sin(2 * np.pi * frequency1 * t)
sin_wave2 = amplitude2 * np.sin(2 * np.pi * frequency2 * t)

# Subtract the second sine wave from the first
sub_wave = sin_wave1 - sin_wave2

# Plot the individual sine waves and their subtraction
plt.plot(t, sin_wave1, label='Sine Wave 1')
plt.plot(t, sin_wave2, label='Sine Wave 2')
plt.plot(t, sub_wave, label='Subtraction of Sine Waves')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Subtracting Sine Waves')
plt.legend()
plt.grid(True)
plt.show()

