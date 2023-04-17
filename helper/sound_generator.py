'''
work in progress
'''


import pyaudio
import numpy as np
import matplotlib.pyplot as plt

samples = np.arange(128)

# Scale to 0 ..  2 pi
samples = samples / 128 *2* np.pi
#print(samples)

base = np.sin(2*np.pi* samples)
harmonics = 0.3 * np.sin(2*np.pi*16* samples)
result = base + harmonics
print("Raw generated signal: ", result)

plt.plot(base)
plt.plot(harmonics)
plt.plot(result)
#plt.show()

# Scale to  0 ..1
min_result = min(result)
max_result = max(result)
result_range = max_result - min_result

print('Before scaling min result: {}, max result: {}, range: {}'.format(min_result, max_result, result_range))

# Shift Signal to only positive
result = (result - min_result)

# Scale Signal to 0...1
result = result / result_range
print('After scaling to 0.. 1: min result: {}, max result: {}'.format(min(result), max(result)))

# Scale to 0 ... 1023
result = result * 1023
result = np.asarray(result, dtype=int)

print('{ ')
for value in result:
    print(value, ', ', end='')
print('} ')

print('Minimum value: ', min(result), ' Maximum value: ', max(result))