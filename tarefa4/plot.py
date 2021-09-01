'''
gduarte@home-vm
Created on 20-jul-2021
'''

import os

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"text.usetex": True,
                     "font.family": "serif",
                     "font.size": 22,
                     "font.sans-serif": ["Computer Modern Roman"]})

def tarefa4a():
    c_dict = {50: 'r', 500: 'b', 5000:'k'}
    lw_dict = {50: 1., 500: .5, 5000:.4}
    for N in [50, 500, 5000]:
        os.system(f'./a.o {N} > ziggy{N}.dat')
        t, fl = np.genfromtxt(f'ziggy{N}.dat').T
        plt.plot(t, fl, c=c_dict[N], lw=lw_dict[N],
                 label=f"{N} pulgas")
    
    plt.ylabel(r"$\rho\qquad$", rotation='horizontal', labelpad=20.)
    plt.xlabel(r"$t/N$")
    plt.legend(frameon=False)


def tarefa4b(max_samples=8):
    os.system('echo > b.dat')
    dt_range = np.logspace(0, max_samples, num=max_samples+1, dtype=int)
    for dt in dt_range:
        os.system(f'./b.o {dt} >> b.dat')
    dt, rho, sigma = np.genfromtxt('b.dat').T
    plt.errorbar(np.log10(dt), rho, sigma, capsize=5, ls='', c='k')
    plt.scatter(np.log10(dt), rho, c='k', s=5)
    plt.axhline(0.5, ls='--', c='b')

    plt.xlabel(r"$\log \Delta t$")
    plt.ylabel(r"$\overline \rho$", rotation='horizontal', labelpad=20.)

