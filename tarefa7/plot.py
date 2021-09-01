'''
gduarte@home-vm
Created on 11-ago-2021
'''

def plot_dif_dT():
    T1, m1 = np.genfromtxt('dif_dT.dat').T
    fig = plt.figure(figsize=(9.6, 8.78))
    T1_b = np.where(T1 == T1.min())[0][0]
    plt.plot(T1[T1_b:], m1[T1_b:], c='r', label=r"$dT = +10^{-4}$/MCS")
    plt.plot(T1[:T1_b], m1[:T1_b], c='b', label=r"$dT = -10^{-2}$/MCS")
    plt.tick_params(direction='in', top=True, right=True)
    plt.xlabel(r"$T$")
    plt.ylabel(r"$m$")
    plt.legend(frameon=False)
    plt.tight_layout(pad=0.4)
    plt.savefig('figs/dif_dT.pdf')
    return fig
    

def plot_low_L():
    t, m1, m2 = np.genfromtxt('low_L.dat').T
    fig = plt.figure(figsize=(9.6, 8.78))
    [p1] = plt.plot(t, m1, c='b', label=r"$L=10$")
    [p2] = plt.plot(t, m2, c='r', label=r"$L=40$")
    plt.tick_params(direction='in', top=True, right=True)
    plt.xlabel(r"$t$ [MCS]")
    plt.ylabel(r"$m$")
    plt.legend(frameon=False)
    plt.tight_layout(pad=0.4)
    plt.savefig('figs/low_L.pdf')
    return fig


def plot_dif_L():
    t, m1, m2 = np.genfromtxt('dif_L.dat').T
    fig = plt.figure(figsize=(9.6, 8.78))
    [p1] = plt.plot(t, m1, c='b', label=r"$L=10$")
    [p2] = plt.plot(t, m2, c='r', label=r"$L=40$")
    plt.tick_params(direction='in', top=True, right=True)
    plt.xlabel(r"$t$ [MCS]")
    plt.ylabel(r"$|m|$")
    plt.legend(frameon=False)
    plt.tight_layout(pad=0.4)
    plt.savefig('figs/dif_L.pdf')
    return fig


def plot_dif_temps():
    t, m1, m2 = np.genfromtxt('dif_temps.dat').T
    fig = plt.figure(figsize=(9.6, 8.78))
    [p1] = plt.plot(t, m1, c='b', label=r"$T=2.5$")
    [p2] = plt.plot(t, m2, c='r', label=r"$T=2.0$")
    plt.tick_params(direction='in', top=True, right=True)
    plt.xlabel(r"$t$ [MCS]")
    plt.ylabel(r"$|m|$")
    plt.legend(frameon=False)
    plt.tight_layout(pad=0.4)
    plt.savefig('figs/dif_temps.pdf')
    return fig


def plot_dif_ci():
    t, m1, m2, m3 = np.genfromtxt('dif_ci.dat').T
    fig = plt.figure(figsize=(9.6, 8.78))
    [p1] = plt.plot(t, m1, c='b', label=r"$S_i = +1$") # ferro_u
    [p2] = plt.plot(t, m2, c='r', label=r"$S_i$ aleatórios") # para
    [p3] = plt.plot(t, m3, c='k', label=r"$S_i$ aleatórios") # para
    plt.tick_params(direction='in', top=True, right=True)
    plt.xlabel(r"$t$ [MCS]")
    plt.ylabel(r"$m$")
    plt.legend(frameon=False)
    plt.tight_layout(pad=0.4)
    plt.savefig('figs/dif_ci.pdf')
    return fig


if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    plt.rcParams.update({"text.usetex": True,
                         "font.family": "serif",
                         "font.size": 22,
                         "font.sans-serif": ["Computer Modern Roman"]})

