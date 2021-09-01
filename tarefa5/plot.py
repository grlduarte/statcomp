'''
gduarte@home-vm
Created on 03-ago-2021
'''

import os

import numpy as np
import matplotlib.pyplot as plt


def gaussian(x, xmed=5, var=4):
    return 1/np.sqrt(2*np.pi*var) * np.exp(-(x-xmed)**2 / (2*var)) 


def parte_a():
    bins = [5, 10, 20, 50]
    fig = plt.gcf()
    fig.clf()
    ax = fig.subplots(2, 2, sharex=True, sharey=True)
    ax = np.reshape(ax, 4)

    for i,b in enumerate(bins):
        os.system(f"./a.out {b} > a.dat")
        xbins, freq = np.genfromtxt('a.dat').T
        x = np.linspace(0, 10, 1000)

        ax[i].bar(xbins, freq, width=10/b, color='wheat',
                  edgecolor='k', alpha=.5, label=f"{b} bins")
        ax[i].plot(x, gaussian(x), c='b', lw=2., ls='--')
        ax[i].legend(frameon=False)
    fig.suptitle("1000 histórias")
    fig.tight_layout()


def parte_b():
    bins = [5, 10, 20, 50]
    fig = plt.gcf()
    fig.clf()
    ax = fig.subplots(2, 2, sharex=True, sharey=True)
    ax = np.reshape(ax, 4)

    for i,b in enumerate(bins):
        os.system(f"./b.out {b} > b.dat")
        xbins, freq = np.genfromtxt('b.dat').T
        x = np.linspace(0, 8, 1000)

        ax[i].bar(xbins, freq, width=8/b, color='wheat',
                  edgecolor='k', alpha=.5, label=f"{b} bins")
        ax[i].plot(x, np.exp(-x), c='b', lw=2., ls='--')
        ax[i].set_yscale('log')
        ax[i].minorticks_off()
        ax[i].legend(frameon=False)
    fig.suptitle("1e6 histórias")
    fig.tight_layout()


if __name__ == "__main__":
    plt.rcParams.update({"text.usetex": True,
                         "font.family": "serif",
                         "font.size": 16,
                         "font.sans-serif": ["Computer Modern Roman"]})

    from matplotlib.backends.backend_pdf import PdfPages
    pdf = PdfPages('resultado.pdf')
    fig = plt.figure(figsize=(9.6, 8.78))

    parte_a()
    pdf.savefig()
    parte_b()
    pdf.savefig()
    pdf.close()
