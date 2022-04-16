from matplotlib import pylab
from matplotlib import pyplot as plt
import numpy as np
from scipy.signal import hilbert, chirp

n = np.linspace(-4, 4, 24000)

a1 = 5
a2 = 5

f1=10.5
f2=9.5

sin1 = a1 * np.sin(f1 * n * np.pi)
sin2 = a2 * np.sin(f2 * n * np.pi)
wave = sin1 + sin2

analytic_signal = hilbert(wave)
amplitude_envelope_up = np.abs(analytic_signal)
amplitude_envelope_down = -1*np.abs(analytic_signal)

fig, axes = plt.subplots(1, 1, figsize = (10, 6), facecolor='w')
axes.axhline(y=0, color='k', alpha=0.7)
axes.grid(True, which='both')
axes.axvline(x=0, color='k', alpha=0.7)
axes.scatter(n, wave, s = 1, c = 'r', marker = '.')
axes.scatter(n, amplitude_envelope_up, s = 1, c = 'g', marker = '.', alpha=0.7)
axes.scatter(n, amplitude_envelope_down, s = 1, c = 'g', marker = '.', alpha=0.7)
axes.set_xlabel("x", fontsize=18)
axes.set_ylabel("y", fontsize=18)
plt.legend(['Beat', 'Hilbert'], loc='upper right', fontsize=14)
axes.tick_params(axis='both', which='major', labelsize=18)

plt.axis([-4, 4, -10, 10])
filename = str(105_95)
plt.savefig(filename + ".jpg")