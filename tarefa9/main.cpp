#include<iostream>
#include<fstream>
#include<math.h>
#include"ising.h"

#define T_MAX 1e5


void binder(int L){
    char fname[20];
    sprintf(fname, "output_L%d.dat", L);
    ofstream output_file(fname);
    Ising2D ferro (L);
    double N = L*L;
    output_file << "#T\tB\n";
    for(float T=2.; T<=3; T+=.01){
        double mag=0, mag2=0, mag4=0;
        ferro.set_temperature(T);
        for(int t=0; t<T_MAX; t++){
            ferro.mc_step();
            double m_S = ferro.calc_magn()/N;
            mag += fabs(m_S)/T_MAX;
            mag2 += m_S*m_S/T_MAX;
            mag4 += pow(m_S, 4)/T_MAX;
        }
        float binder = 1 - 1./3 * mag4/mag2/mag2;
        output_file << ferro.temp() << '\t';
        output_file << binder << '\n';
    }
    output_file.close();
}

int main(){
    binder(5);
    binder(10);
    binder(20);
}
