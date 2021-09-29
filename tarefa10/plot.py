'''
gduarte@home-vm
Created on 27-set-2021
'''

import matplotlib.pyplot as plt
import numpy as np


def plot_data(fname='output_L200_T2.0.dat'):
    fig = plt.figure(figsize=(9.6, 8.78))
    fig.suptitle(r"$L = 200$\quad$T = 2.0$")
    t, metropolis, kawasaki = np.genfromtxt(fname).T
    plt.scatter(t, metropolis, marker='o', c='r', label='Metropolis')
    plt.plot(t, t**(1/2), c='k', lw=1., label=r'$t^{1/2}$')
    plt.scatter(t, kawasaki, marker='x', c='b', label='Kawasaki')
    plt.plot(t, t**(1/3), c='k', lw=1., label=r'$t^{1/3}$')

    ax = plt.gca()
    ax.set_xlim(1e2, 1e4)
    ax.set_xscale('log')
    ax.set_xticklabels([f"{val:.0f}" for val in ax.get_xticks()])
    ax.set_xlabel(r'$t$ (MCS)')
    
    ax.set_ylim(5, 150)
    ax.set_yscale('log')
    ax.set_yticklabels([f"{val:.0f}" for val in ax.get_yticks()])
    ax.set_ylabel(r'$R_e (t)$')

    ax.tick_params(which='both', direction='in', top=True, right=True)
    ax.legend(frameon=False)
    fig.tight_layout(pad=.4)
    fig.savefig(fname.replace('.dat', '.pdf'))
    plt.close()


if __name__ == '__main__':
    plt.rcParams.update({"text.usetex": True,
                         "font.family": "serif",
                         "font.size": 16,
                         "font.sans-serif": ["Computer Modern Roman"]})
    plot_data()
