# -*- coding: utf-8 -*-
"""
Spyder Editor

@author: mylinux

This is a temporary script file.
"""

import DSP as dsp
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile


Fs=500.0; T=1/Fs; Nd=500; Nfft=2000;

# Signal frequencies
freq=np.array([55,100]);

# Signal amplitudes
Amp=np.array([3.0,5.0]);

# data point vector
n=np.arange(0,Nd)


# angular frequencies
w0=2*np.pi*freq[0]/Fs
w1=2*np.pi*freq[1]/Fs

# signals that are combined together
signal_sin_0=Amp[0]*np.sin(w0*n)
signal_sin_1=Amp[1]*np.sin(w1*n)

dc_sig=np.ones(Nd)*1

awgn=np.random.random(Nd)*5

# combine signals
sig=signal_sin_0 + signal_sin_1 + awgn + dc_sig

# time vector
time=n*T


# plot combined sine wave
plt.figure()
plt.plot(time,sig,color='blue', linewidth=0.75)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [Au]')
plt.title('Combined Signal')
plt.grid()



#plot FFT - Fast Fourier Transform
dsp.plotFFT(sig, Fs, Nfft, Nd)


order=4
pbr=0.5
msba=40
fCut=60
Type='low'

b,a=dsp.designEllip(Fs,order,pbr,fCut,msba,Type)



filteredSignal = (scipy.signal.lfilter(b, a, sig))


plt.figure()
plt.plot(time,filteredSignal,color='blue', linewidth=0.75)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [Au]')
plt.title('Combined Signal')
plt.grid()

#plt.figure()
dsp.plotFFT(filteredSignal, Fs, Nfft, Nd)

plt.figure()
dsp.plotAmplitudeResponse(b,a, Fs)
