'''
gduarte@home-vm
Created on 18-ago-2021
'''

from collections import OrderedDict

from numba import jit, int64, float64
from numba.experimental import jitclass
import numpy as np
ranf = np.random.rand


spec = {'L': int64, 'N': int64, 't_mcs': int64,
        'T': float64, 'h': float64,
        '_u': int64[:], '_d': int64[:],
        '_l': int64[:], '_r': int64[:],
        'lattice': int64[:],}


@jitclass(OrderedDict(spec))
class Ising2D:
    '''
    Metropolis algorithm implementation of a
    2-dimensional Ising model with periodic 
    boundary conditions.
    
    Parameters
    ----------
    L : int
        Size of the lattice.
    temp : float, optional
        Temperature of the lattice. Default is 2.
    initial : int, optional
        Initial conditions:
            -1 : all spins down   
             0 : random spins
            +1 : all spins up (default)
    '''
    def __init__(self, L, temp=2., initial=+1):
        self.L = L
        self.N = L*L
        self.T = temp
        self.t_mcs = 0
        self.h = 0
        self.set_initial(initial)
        self._set_indices()

    def _set_indices(self):
        u = np.empty(self.N, dtype=int64) 
        d = np.empty(self.N, dtype=int64) 
        l = np.empty(self.N, dtype=int64) 
        r = np.empty(self.N, dtype=int64) 
        L = self.L
        for i in range(self.N):
            y = i%L; x = (i-i%L)//L
            u[i] = (y + ((x+L-1)%L)*L)
            d[i] = (y + ((x+1)%L)*L)
            l[i] = ((y+L-1)%L + x*L)
            r[i] = ((y+1)%L + x*L)
        self._u = u
        self._d = d
        self._l = l
        self._r = r

    def set_initial(self, ci):
        if (abs(ci) == 1):
            self.lattice = np.array([ci for _ in range(self.N)])
        elif (ci == 0):
            self.lattice = np.array([1 if (ranf()>.5) else -1 for _ in range(self.N)])
        else:
            raise ValueError(
            """ci must be:
                  -1 : all spins down
                   0 : random spins
                  +1 : all spins up""")

    def set_temp(self, temp):
        self.T = temp

    def set_field(self, field):
        self.h = field

    def calc_energy(self):
        s = 0
        for i in range(self.N):
            d = self._d[i]
            r = self._r[i]
            s -= self.lattice[i] * (self.lattice[d] + self.lattice[r])
        return s

    def calc_magn(self):
        s = 0
        for i in range(self.N):
            s += self.lattice[i]
        return s

    def flip_spin(self, i):
        l = self._l[i]
        r = self._r[i]
        u = self._u[i]
        d = self._d[i]
        d_energy = (self.lattice[u] + self.lattice[d] + self.lattice[l] + self.lattice[r] + self.h)
        d_energy *= 2. * self.lattice[i]
        if (d_energy <= 0.) | (ranf() < np.exp(-d_energy/self.T)):
            self.lattice[i] *= -1
            return 1
        else: return 0

    def mc_step(self):
        for t in range(self.N):
            i = int(ranf() * self.N)
            self.flip_spin(i)
        self.t_mcs += 1
        return self.t_mcs
        
