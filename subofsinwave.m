% Define the parameters for the first sine wave
amplitude1 = 1;
frequency1 = 2;  % in Hz

% Define the parameters for the second sine wave
amplitude2 = 0.5;
frequency2 = 3;  % in Hz

% Define the common parameters
duration = 1;  % in seconds
sampling_rate = 1000;  % in samples per second

% Generate the time vector
t = 0:1/sampling_rate:duration-1/sampling_rate;

% Generate the sine waves
sin_wave1 = amplitude1 * sin(2 * pi * frequency1 * t);
sin_wave2 = amplitude2 * sin(2 * pi * frequency2 * t);

% Subtract the second sine wave from the first
sub_wave = sin_wave1 - sin_wave2;

% Plot the individual sine waves and their subtraction
plot(t, sin_wave1, 'DisplayName', 'Sine Wave 1');
hold on;
plot(t, sin_wave2, 'DisplayName', 'Sine Wave 2');
plot(t, sub_wave, 'DisplayName', 'Subtraction of Sine Waves');
hold off;
xlabel('Time (s)');
ylabel('Amplitude');
title('Subtracting Sine Waves');
legend;
grid on;

