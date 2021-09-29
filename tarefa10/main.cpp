#include<iostream>
#include<fstream>
#include<math.h>
#include"ising.h"

#define L 200
#define T 2.0
#define eT -1.745564575312553
#define T_MAX 1e4

int main(){
    char fname[20];
    sprintf(fname, "output_L%d_T%.1f.dat", L, T);
    ofstream ofile(fname);

    Ising2D para (L, T);
    Ising2D para_k (L, T);
    para.set_initial(0);
    para_k.set_initial(0);
    double N = L*L;
    ofile << "#T\tRe\tRe_kawasaki\n";
    para.set_temperature(T);
    for(int t=0; t<T_MAX; t++){
        para.mc_step();
        para_k.mcs_kawasaki();
        if (t%100 == 0){
            double e_S;
            ofile << t << '\t';
            e_S = para.calc_energy()/N;
            ofile << 2./(e_S-eT) << '\t';
            e_S = para_k.calc_energy()/N;
            ofile << 2./(e_S-eT) << '\n';
        }
    }
    ofile.close();
}
