# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:01:06 2020

@author: james
"""

import matplotlib.pyplot as plt
import numpy as np
import math

fc = 100/math.pi
x = np.arange(0.1 * fc, 20 * fc, 1)#frequency
omega = 2 * math.pi * x
y= 1/(1+(omega * 0.005) ** 2)**0.5 #magnitude (dB)


plt.plot(x,y)
plt.xscale('log')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.title('Bode Plot of RC Low-Pass Filter')

plt.plot(fc,1/2**0.5,'ko', label= 'Cutoff frequency')

plt.legend()


plt.show()