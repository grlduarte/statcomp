#include<iostream>
#include<math.h>

#include"ising.h"

#define L 5
#define T_MAX 1e6

int main(){
    Ising2D ferro (L);
    double N = L*L;
    cout << "#T\te\t|m|\tchi\tc_v\n";
    for(float T=.1; T<=5; T+=.05){
        double mag=0, mag2=0, e=0, e2=0;
        ferro.set_temperature(T);
        for(int t=0; t<T_MAX; t++){
            ferro.mc_step();
            double e_S = ferro.calc_energy()/N;
            double m_S = ferro.calc_magn()/N;
            mag += fabs(m_S)/T_MAX;
            mag2 += m_S*m_S/T_MAX;
            e += e_S/T_MAX;
            e2 += e_S*e_S/T_MAX;
        }
        cout << ferro.temp() << '\t';
        cout << e << '\t';
        cout << mag << '\t';
        cout << N/T * (mag2 - mag*mag) << '\t';
        cout << N/T/T * (e2 - e*e) << '\n';
    }
}
