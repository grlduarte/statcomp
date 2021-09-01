'''
gduarte@home-vm
Created on 18-ago-2021
'''

import numpy as np

from ising import Ising2D

if __name__ == '__main__':
    L = 5
    N = L*L
    t_max = 1e5
    temps = np.arange(.1, 5., .05)
    dados = {'T': [], 'e': [], 'm': [], 'chi': [], 'c_v': []}

    print("#T\te\t|m|\tchi\tc_v\t")
    ferro = Ising2D(L)
    for T in temps:
        ferro.T = T
        m=0; m2=0; e=0; e2=0
        for t in range(int(t_max)):
            ferro.mc_step()
            e_S = ferro.calc_energy()/N
            m_S = ferro.calc_magn()/N
            e += e_S / t_max
            e2 += e_S*e_S / t_max
            m += np.fabs(m_S) / t_max
            m2 += m_S*m_S / t_max
        out = ""
        out += f"{T:.5f}\t"
        out += f"{e:.5f}\t"
        out += f"{m:.5f}\t"
        out += f"{(N/T * (m2 - m*m)):.5f}\t"
        out += f"{(N/T/T * (e2 - e*e)):.5f}\t"
        print(out)

