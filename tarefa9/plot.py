'''
gduarte@home-vm
Created on 27-set-2021
'''

import matplotlib.pyplot as plt
import numpy as np


def read_data():
    T, B5 = np.genfromtxt('output_L5.dat').T
    T, B10 = np.genfromtxt('output_L10.dat').T
    T, B20 = np.genfromtxt('output_L20.dat').T
    data = [T, {'L = 5': B5, 'L = 10': B10, 'L = 20': B20}]
    return data


def plot_data(data, fname='resultado.pdf'):
    fig = plt.figure(figsize=(9.6, 8.78))
    x_label = 'T'
    y_label = 'B'
    x = data[0]
    for label, y in data[1].items():
        plt.plot(x, y, lw=1., label=label)
    plt.axvline(2.269, c='k', lw=2., ls='--', label=r'$T_C=2.269$')
    plt.xlabel('T')
    plt.ylabel('Cumulante de Binder')
    plt.tick_params(direction='in', top=True, right=True)
    fig.tight_layout(pad=.4)
    plt.legend(frameon=False)
    plt.savefig(fname)
    plt.close()
 

if __name__ == '__main__':
    plt.rcParams.update({"text.usetex": True,
                         "font.family": "serif",
                         "font.size": 16,
                         "font.sans-serif": ["Computer Modern Roman"]})
    d = read_data()
    plot_data(d)

