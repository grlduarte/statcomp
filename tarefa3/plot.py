'''
gduarte@home-vm
Created on 13-jul-2021
'''

import os

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages
from scipy.optimize import curve_fit

N_HIST = [10, 100, 1000, 5000]
def f(x, a, b):
    return a*x + b

if __name__ == '__main__':
    with PdfPages('resultado.pdf') as pdf:
        for i, n in enumerate(N_HIST):
            plt.figure(figsize=(7,7))
            os.system(f'./main.o {n:.0f} > walk.dat')
            n_hist = np.genfromtxt('walk.dat', max_rows=1)
            t, x2, sig = np.genfromtxt('walk.dat', skip_header=1).T
        
            plt.fill_between(t, x2-sig, x2+sig, color='orange', alpha=.25)
            plt.plot(t, x2, c='k', lw=1.5)
            plt.title(f'N_HIST = {n_hist:.0f}')
            plt.xlabel("dt")
            plt.ylabel("<x2>")
        
            popt, _ = curve_fit(f, t, x2)
            plt.plot(t, f(t, *popt), c='b', ls='--', label=f'coef angular = {popt[0]:.2f}')
            plt.legend(frameon=False, loc='lower right')

            plt.tight_layout()
            pdf.savefig()
            plt.close()
