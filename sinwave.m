% Define the parameters
amplitude = 1;
frequency = 2;  % in Hz
duration = 1;  % in seconds
sampling_rate = 1000;  % in samples per second

% Generate the time vector
t = 0:1/sampling_rate:duration-1/sampling_rate;

% Generate the sine wave
sin_wave = amplitude * sin(2 * pi * frequency * t);

% Plot the sine wave
plot(t, sin_wave);
xlabel('Time (s)');
ylabel('Amplitude');
title('Sine Wave');
grid on;

