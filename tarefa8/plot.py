'''
gduarte@home-vm
Created on 07-ago-2021
'''


prop_label = {0:r"$T$", 1:r"$<e>$", 2:r"$<|m|>$", 3:r"$\chi$", 4:r"$c_V$"}


def read_data():
    prop = {}
    for k in prop_label:
        prop.update({k: {}})

    fnames = ['exata', 'metropolis']
    for f in fnames:
        t = np.genfromtxt(f+'.dat').T
        for k in prop_label:
            prop[k].update({f: t[k]})
    return prop


def plot_data(data, fname='resultado.pdf'):
    pdf = PdfPages(fname)
    x_label = prop_label[0]
    x1 = data[0]['exata']
    x2 = data[0]['metropolis']
    for k in prop_label:
        if k > 0:
            fig = plt.figure(figsize=(9.6, 8.78))
            y_label = prop_label[k]
            y1 = data[k]['exata']
            y2 = data[k]['metropolis']
            plt.plot(x2, y2, c='k', lw=3., ls='--', label='Algoritmo de Metropolis')
            plt.plot(x1, y1, c='b', lw=1., label='Solução exata')
            plt.xlabel(x_label)
            plt.ylabel(y_label)
            plt.tick_params(direction='in', top=True, right=True)
            fig.tight_layout()
            plt.legend(frameon=False)
            pdf.savefig()
            plt.close()
    pdf.close()
    

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_pdf import PdfPages
    plt.rcParams.update({"text.usetex": True,
                         "font.family": "serif",
                         "font.size": 16,
                         "font.sans-serif": ["Computer Modern Roman"]})

    p = read_data()
    plot_data(p)
