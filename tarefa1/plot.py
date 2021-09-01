'''
gduarte@home-vm
Created on 29-jun-2021
'''

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    n, med, stdev = np.genfromtxt('results.dat').T
    plt.plot(n, med, c='k', lw=1.5)
    plt.fill_between(n, med-stdev, med+stdev, color='orange', alpha=.25)
    plt.title(f"N_MAX = {n.max():.0f}")
    plt.axhline(0.5, ls='--', lw=1, zorder=-1)
