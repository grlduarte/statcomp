'''
gduarte@home-vm
Created on 29-set-2021
'''

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from mpl_toolkits.axes_grid.inset_locator import (inset_axes, InsetPosition,
                                                  mark_inset)
import numpy as np


def plot_espaco_fase(pdf, data):
    fig = plt.figure(figsize=(9.6, 8.78))
    for k, d in data.items():
        t, x, v, dE = d
        plt.plot(x, v, label=k, c=c[k], lw=lw[k], ls=ls[k])
    ax = plt.gca()
    ax.legend(frameon=False)
    ax.set_xlabel(r'$x (t)$')
    ax.set_ylabel(r'$v (t)$')
    ax.tick_params(which='both', direction='in', top=True, right=True)
    fig.tight_layout(pad=.4)
    pdf.savefig()
    plt.close()


def plot_delta_energia(pdf, data):
    fig, ax1 = plt.subplots(figsize=(9.6, 8.78))
    for k, d in data.items():
        t, x, v, dE = d
        ax1.plot(t, dE, label=k, c=c[k], lw=lw[k], ls=ls[k])
    ax1.legend(frameon=False)
    ax1.set_xlabel(r'$t$')
    ax1.set_ylabel(r'$\Delta E/E_0 (t)$')
    ax1.tick_params(which='both', direction='in', top=True, right=True)
    ax1.set_xlim(0, 100)
    ax1.set_ylim(-10, 150)

    ax2 = plt.axes([0,0,1,1])
    ip = InsetPosition(ax1, [.15,.2,.3,.3])
    ax2.set_axes_locator(ip)
    for k, d in data.items():
        t, x, v, dE = d
        ax2.plot(t, dE, c=c[k], lw=lw[k], ls=ls[k])
    ax2.tick_params(which='both', direction='in', top=True, right=True)
    ax2.set_xlim(0, 10)
    ax2.set_ylim(-.05, .05)

    fig.tight_layout(pad=.4)
    pdf.savefig()
    plt.close()


if __name__ == "__main__":
    data = {}
    data['Euler'] = np.genfromtxt('ohs_euler.dat').T
    data['Euler-Cromer'] = np.genfromtxt('ohs_euler_cromer.dat').T
    data['Velocity-Verlet'] = np.genfromtxt('ohs_velocity_verlet.dat').T
    ls = {'Euler': '--', 'Euler-Cromer': '-.', 'Velocity-Verlet': '-'}
    lw = {'Euler': 1., 'Euler-Cromer': 1., 'Velocity-Verlet': 1.}
    c = {'Euler': 'k', 'Euler-Cromer': 'r', 'Velocity-Verlet': 'b'}

    plt.rcParams.update({"text.usetex": True,
                         "font.family": "serif",
                         "font.size": 16,
                         "font.sans-serif": ["Computer Modern Roman"]})
    pdf = PdfPages('resultado.pdf')
    plot_espaco_fase(pdf, data)
    plot_delta_energia(pdf, data)
    pdf.close()
