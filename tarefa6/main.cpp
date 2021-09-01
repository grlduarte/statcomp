#define L 5

#include<iostream>
#include<math.h>
#include"site.hpp"

using namespace std;


void print_lattice(Site lattice[L][L]){
    for(int i=0; i<L; i++){
        for(int j=0; j<L; j++)
            cout << lattice[i][j].site_spin() << '\t';
        cout << '\n';
    }
}


float calc_energy(Site lattice[L][L]){
    float sum = 0;
    for(int i=0; i<L; i++){
        for(int j=0; j<L; j++)
            sum += lattice[i][j].site_energy();
    }
    return -sum;
}


float calc_magn(Site lattice[L][L]){
    int sum = 0;
    for(int i=0; i<L; i++){
        for(int j=0; j<L; j++)
            sum += lattice[i][j].site_spin();
    }
    return sum;
}


void spin_state(int spin[L][L], unsigned long n){
    for(int k=0; k<L*L; k++){
        int bit = (n & ( 1 << k )) >> k;
        spin[k%L][(k - k%L)/L] = 2*bit - 1;
    }
}


void calc_properties(int spin[L][L], Site lattice[L][L], double T){
    unsigned long state = 0;
    double w, N=L*L, z=0, e=0, e2=0, m=0, m2=0;
    long state_max = pow(2, N); // last state is 2**N - 1
    
    while(state < state_max){
        spin_state(spin, state);
        double e_S = calc_energy(lattice);
        int m_S = calc_magn(lattice);
        w = exp(-e_S/T);

        z += w;                             // funcao de equiparticao
        e += (e_S/N) * w;                   // energia por spin
        e2 += (e_S*e_S/N/N) * w;            // energia ao quadrado por spin
        m += fabs((float) m_S/N) * w;       // magnetizacao abs por spin
        m2 += ((float) m_S*m_S/N/N) * w;    // magnetizacao ao quadrado por spin
        state++;
    }
    e /= z;
    m /= z;
    e2 /= z;
    m2 /= z;
    // print T, e, |m|, chi, c_v, f
    cout << T << '\t';
    cout << e << '\t';
    cout << m << '\t';
    cout << N/T * (m2 - m*m) << '\t';
    cout << N/T/T * (e2 - e*e) << '\t';
    cout << -T/N * log(z) << '\n';
}


int main(){
    int spin[L][L];
    Site lattice[L][L];

    // initialize addresses
    for(int i=0; i<L; i++){
        for(int j=0; j<L; j++)
            lattice[i][j].init(spin, i, j);
    }

    double T;
    cout << "#T\te\tabs(m)\tchi\tc_v\tf\n";
    for(T=0.1; T<.2; T+=.1){
        calc_properties(spin, lattice, T);
    }
}
