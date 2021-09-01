'''
gduarte@home-vm
Created on 07-ago-2021
'''


prop_label = {0:r"$T$", 1:r"$<e>$", 2:r"$<|m|>$", 3:r"$\chi$", 4:r"$c_V$", 5:r"$f$"}


def read_data():
    prop = {}
    for k in prop_label:
        prop.update({k: {}})

    N_range = [2, 3, 4, 5,]
    for N in N_range:
        t = np.genfromtxt(f'results{N}.dat').T
        for k in prop_label:
            prop[k].update({N: t[k]})
    return prop


def plot_data(data, fname='resultado.pdf'):
    pdf = PdfPages(fname)
    x = data[0][2]
    x_label = prop_label[0]
    for k in prop_label:
        if k > 0:
            fig = plt.figure(figsize=(9.6, 8.78))
            y_label = prop_label[k]
            for N in data[k]:
                y = data[k][N]
                plt.plot(x, y, lw=1., label=N)
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
