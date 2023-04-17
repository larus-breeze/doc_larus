'''
work in progress. 
'''

import matplotlib.pyplot as plt
import numpy as np
#  https://flothesof.github.io/Karplus-Strong-algorithm-Python.html


def synthesize(sampling_speed, wavetable, n_samples):
    """Synthesizes a new waveform from an existing wavetable."""
    samples = []
    current_sample = 0
    while len(samples) < n_samples:
        current_sample += sampling_speed
        current_sample = current_sample % wavetable.size
        samples.append(wavetable[current_sample])
        current_sample += 1
    return np.array(samples)



# Sinus wavetable
n_samples = 128
t = np.linspace(0, 1, num=n_samples)
wavetable = np.sin(np.sin(2 * np.pi * t))

# Triangle
wavetable = t * (t < 0.5) + (-(t - 1)) * (t>= 0.5)




sample1 = synthesize(1, wavetable, n_samples)

plt.plot(sample1)


plt.show()