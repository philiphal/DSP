# -*- coding: utf-8 -*-
"""
@author: mylinux

Uses numpy, matplotlib and scipy 
for simple dsp techniques


Filtering and FFT Functionality

"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

'''**********************************************************************'''
'''	                           FFT FUNCTION                             '''
'''**********************************************************************'''
def plotFFT(sig, Fs, Nfft, Nd):
    X = np.fft.fft(sig,Nfft)
    Xmag = np.abs(X[0:int(Nfft/2)])
    ''' calibrate for amplitude'''
    Xcal = Xmag*2/Nd
    ''' calibrate for freq spacing '''
    freqSpacing = Fs/Nfft
    ''' scale x-axis with freqspacing '''
    f = np.arange(0,Nfft/2)*freqSpacing
    ''' plot (x,y) '''
    plt.figure()
    plt.plot(f,(Xcal),'r')
    plt.grid()
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Amplitude [Au]')
    plt.title(' Calibrated %d point FFT'%(Nfft))

'''**********************************************************************'''
'''                     DC notch to remove DC offset                     ''' 
'''**********************************************************************'''
def dcNotch():
    b = np.array([1.0,-1.0])
    a = np.array([1.0,-0.95])
    
    return(b,a)
    

'''**********************************************************************'''
'''             First order recursive for smoothing rectified signal     '''
'''                     (can be used to generate envelope)               ''' 
'''**********************************************************************'''    
def firstOrderRecursive():
    b = np.array([0.001])
    a = np.array([1.0,-0.999])
    
    return(b,a)
    

'''**********************************************************************'''
'''             returns b, a coefficients for a Butterworth              ''' 
'''**********************************************************************'''
def designButterWorth(filter_order, fCut, Fs, Type):
    nyquist = 0.5 * Fs
    normal_cutoff = fCut/nyquist
    b, a = signal.butter(filter_order, normal_cutoff, btype=Type)
    return (b,a)
    
   
'''**********************************************************************'''
'''             returns b,a coefficients for an Eliptic                  ''' 
'''**********************************************************************'''    
def designEllip(Fs,filter_order, filter_pbr,fCut, filter_msba,Type): 
    '''elliptic filter parameters '''
    nyquist = 0.5 * Fs
    normal_cutoff = fCut/nyquist
    b,a=signal.ellip(filter_order, filter_pbr, filter_msba, normal_cutoff, btype=Type)   
    return (b,a)
    
    
'''********************************************************************'''
'''              Plots amplitude response of b,a coefficents           ''' 
'''********************************************************************'''  
def plotAmplitudeResponse(b,a, Fs):
    w, h = signal.freqz(b, a, 50)
    plt.plot((Fs*0.5/np.pi)*w,  20*np.log10(np.abs(h)), 'b')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude [dB]')
    plt.ylim(-50,3)
    plt.xlim(0,Fs/2)
    plt.title("Filter Magnitude Response ")
    plt.grid()


