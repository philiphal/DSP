# -*- coding: utf-8 -*-
"""
@author: mylinux

Uses numpy, matplotlib and scipy 
for simple dsp techniques

"""

import DSP as dsp
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile

# Variables for Sampling Frequency, time value,
# number of data points & nomber of FFT coefficients
Fs=500.0; T=1/Fs; Nd=500; Nfft=2000;

# Array of two signal frequencies 55 & 100 Hz
freq=np.array([55,100]);

# Array of two signal amplitudes 3 & 5 Au
Amp=np.array([3.0,5.0]);

# data point vector
n=np.arange(0,Nd)

# creat time vector
time=n*T

# angular frequencies
w0=2*np.pi*freq[0]/Fs
w1=2*np.pi*freq[1]/Fs

# sinusoidal signals that are combined together
signal_sin_0 = Amp[0]*np.sin(w0*n)
signal_sin_1 = Amp[1]*np.sin(w1*n)

# DC offset
dc_level = 5.0
dc_sig = np.ones(Nd)*dc_level


# Addititve white Gaussian noise
awgn = np.random.random(Nd)*5


# combine signals, awgn & noise
sig = signal_sin_0 + signal_sin_1 + dc_sig + awgn



# plot combined signal - time domain
plt.figure()
plt.plot(time, sig, color='blue', linewidth=0.75)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [Au]')
plt.title('Combined Signal')
plt.grid()



#plot FFT - Fast Fourier Transform of combined signal
dsp.plotFFT(sig, Fs, Nfft, Nd)



# initialise parameters for an elliptic low-pass

# filter order
elip_order = 4

# pass-band ripple
elip_pbr = 0.5

#minimum stop-band attenuation
elip_msba = 40

# Cut frequency
elip_fCut = 60

# Frequency type
elip_Type='low'


# call  filter design function to obtain b, a coefficients
b, a = dsp.designEllip(Fs, elip_order, elip_pbr, elip_fCut, elip_msba, elip_Type)


#plot amplitude response of the filter
plt.figure()
dsp.plotAmplitudeResponse(b, a, Fs)

# filter signal using b, a coefficients
filteredSignal = (scipy.signal.lfilter(b, a, sig))


# plot filtered signal - time domain
plt.figure()
plt.plot(time, filteredSignal, color='blue', linewidth=0.75)
plt.xlabel('Time [s]')
plt.ylabel('Amplitude [Au]')
plt.title('Filtered Signal')
plt.grid()

#plot FFT - Fast Fourier Transform of filtered signal
dsp.plotFFT(filteredSignal, Fs, Nfft, Nd)


