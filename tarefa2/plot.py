'''
gduarte@home-vm
Created on 29-jun-2021
'''

import os
import sys

import matplotlib.pyplot as plt
import numpy as np

class Sorteio:
    def __init__(self, n=None, N=None, p=0.5):
        try:
            n = int(n)
        except:
            n = 5
    
        try:
            N = int(N)
        except:
            N = int(5e3)
    
        os.system('./main.o {} {:.0f} > hist.dat'.format(n, N))
        t = np.genfromtxt('hist.dat')
        self.p = p
        self.N = t[-1]
        self.hist = t[:-1]
        self.n = self.hist.shape[0]-1
        self.x = np.arange(self.hist.shape[0])

    def make_histogram(self, ax):
        ax.bar(self.x, self.hist/self.N,
               width=1, color='wheat', edgecolor='k', linewidth=.4, 
               alpha=1, label='%d flips' %self.n)

        sig2 = self.n * self.p * (1-self.p)
        x_g = np.arange(self.x[0], self.x[-1], (self.x[-1]-self.x[0])/500)
        g = 1/np.sqrt(2*np.pi*sig2) * np.exp(-(x_g-self.n*self.p)**2 / (2*sig2)) 
        ax.plot(x_g, g, c='k', lw=2, label=r'$\sigma^2 = %.2f$' %sig2)

        return ax

if __name__ == '__main__':
    hist5 = Sorteio(n=5)
    hist50 = Sorteio(n=50)
    hist500 = Sorteio(n=500)

    fig = plt.figure()
    ax = [0,0,0]
    ax[0] = plt.subplot(221)
    ax[1] = plt.subplot(222)
    ax[2] = plt.subplot(212)

    ax[0] = hist5.make_histogram(ax[0])
    ax[1] = hist50.make_histogram(ax[1])
    ax[2] = hist500.make_histogram(ax[2])

    fig.suptitle(f'{int(hist5.N)} histórias')
    for ax0 in ax:
        ax0.legend()
        ax0.grid(alpha=0.25)
        ax0.tick_params(direction='in',
                        top=True, right=True)

