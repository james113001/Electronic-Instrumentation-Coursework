# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 21:35:42 2020

@author: james
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 12:31:02 2020

@author: james
"""
import matplotlib.pyplot as plt
import numpy as np
import math


#sx/sy = simulated
#mx/my = measured
#ty = theoretical
my, mx = np.loadtxt('4-2 Data.txt', dtype=(float,float), skiprows=3, usecols=(1,2), unpack=True)
mx = [x*math.pi/180 for x in mx]
#convert time
# stopval = mx[0].find('.')
# mx[0]= mx[0][stopval:]
# mx[0]= float(mx[0])
# for i in range(len(mx)):
#     if i == 0:
#         continue
#     mx[i]= float(mx[i][stopval:])
# mx=mx.astype(np.float)
# my=my.astype(np.float)
# mx= mx - mx[0]


fc = 100/math.pi
tx = np.arange(0.1 * fc, 15 * fc, 1)#frequency
w= 2 * math.pi * tx
tphase = [-math.tan(x * 0.005) for x in w]

# ty= 1/(1+(w * 0.005) ** 2)**0.5 #magnitude (dB)
H=1/(1 + 1j*w* 0.005)
MagH=abs(H)
def gain(MagH):
    dB=[]
    for i in MagH:
        dB.append(20 * math.log10(i))
    return dB


# plt.plot(tphase, gain(MagH), label='Theoretical')
# plt.xscale('log')
plt.xlabel('Phase (rad)')
plt.ylabel('Gain (dB)')

#measured
plt.plot(mx,my, 'r-', label= 'Measured')
phases=[6.04, 16.8, 45.6, 68.7, 81.9] 
phase = [x*math.pi/180 for x in phases]
mMagH = gain([0.935, 0.946, 0.687, 0.309, 0.104])

plt.plot(phase, mMagH,'ko', label= 'Oscilloscope')

plt.title('Bode Plot of RC Low-Pass Filter')

#theorecticalv = 1 + (-1)* np.exp(-(mx)/.0047)

#plt.plot(mx,theorecticalv, label= 'Theoretical')

#plt.plot([.00235,.0047,.00705],[.353,.549,.637],'ko', label= 'Measured')

plt.legend()

plt.show()