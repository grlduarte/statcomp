'''
gduarte@home-vm
Created on 30-ago-2021
'''

import numpy as np
from tkinter import Tk, Canvas


from ising import Ising2D


class MetropolisDynamics(Canvas):
    def __init__(self, master, L, temp=2., initial=1):
        self.L = L
        self.grid = Ising2D(self.L, temp, initial)
        self.fill_d = {+1: 'white', -1: 'black'}
        self.scale = 800 // self.L
        self.width = self.scale * self.L
        self.height = self.scale * self.L
        self.screen = np.zeros_like(self.grid.lattice)
        super().__init__(master, width=self.width,
                         height=self.height, bg='white')
        self.pack()

    def start(self):
        self.counter = 0
        self.step()

    def step(self):
        self.grid.mc_step()
        self.counter += 1
        if self.counter == self.L:
            self.draw_screen()
            self.counter = 0
        self.ident = self.after(1, self.step)

    def draw_screen(self):
        for i in range(self.L**2):
            self.delete(self.screen[i])
            s = self.grid.lattice[i]
            y = i % self.L
            x = (i - y)//self.L
            c = (x*self.scale, y*self.scale)
            c+= ((x+1)*self.scale, (y+1)*self.scale)
            self.screen[i] = self.create_rectangle(c,
                             fill=self.fill_d[s], outline=self.fill_d[s])


if __name__ == '__main__':
    root = Tk()
    dyn = MetropolisDynamics(root, 200, initial=0)
    dyn.start()
    root.mainloop()

