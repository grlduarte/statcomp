#include<iostream>

#include"ising.h"

#define L 100
#define T_FIN 10000

void hist(){
    Ising2D ferro (L);
    ferro.set_initial(-1);
    float dH = 1e-4;
    for(float h=-3; h<3; h+=dH){
        ferro.set_ext_field(h);
        ferro.mc_step();
        cout << h << '\t';
        cout << ferro.calc_magn()/L/L << '\n';
    }
    for(float h=3; h>-3; h-=dH){
        ferro.set_ext_field(h);
        ferro.mc_step();
        cout << h << '\t';
        cout << ferro.calc_magn()/L/L << '\n';
    }
}

void dif_dT(){
    float T_i = 2.2;
    Ising2D ferro (L, T_i);
    ferro.set_initial(1);
    float T = ferro.temp();
    float dT = -1e-1;
    while(true){
        ferro.mc_step(dT);
        T = ferro.temp();
        cout << T << '\t';
        cout << ferro.calc_magn()/L/L << '\n';
        if(T < 0.1) dT = 1e-4;
        else if(T > T_i) break;
    }
}

void low_L(){
    Ising2D ferro (10), ferro2(40);
    cout << "#t\tm1\tm2\n";
    for(int t=0; t<T_FIN; t++){
        ferro.mc_step();
        ferro2.mc_step();
        cout << t << '\t';
        cout << ferro.calc_magn()/100 << '\t';
        cout << ferro2.calc_magn()/1600 << '\n';
    }
}

void dif_Ls(){
    int L1=10, L2=40;
    Ising2D para1(L1), para2(L2);
    para1.set_initial(0);
    para2.set_initial(0);
    cout << "#t\t|m1|\t|m2|\n";
    for(int t=0; t<T_FIN; t++){
        para1.mc_step();
        para2.mc_step();
        cout << t << '\t';
        cout << fabs(para1.calc_magn())/L1/L1 << '\t';
        cout << fabs(para2.calc_magn())/L2/L2 << '\n';
    }
}

void dif_ci(){
    Ising2D ferro_u(L), ferro_d(L), para(L);
    ferro_d.set_initial(-0);
    para.set_initial(0);
    cout << "#t\tm1\tm2\tm3\n";
    for(int t=0; t<T_FIN; t++){
        ferro_u.mc_step();
        ferro_d.mc_step();
        para.mc_step();
        cout << t << '\t';
        cout << ferro_u.calc_magn()/L/L << '\t';
        cout << ferro_d.calc_magn()/L/L << '\t';
        cout << para.calc_magn()/L/L << '\n';
    }
}

void dif_temps(){
    Ising2D ferro (L, 2.5), ferro2 (L, 2.);
    cout << "#t\t|m1|\t|m2|\n";
    for(int t=0; t<T_FIN; t++){
        ferro.mc_step();
        ferro2.mc_step();
        cout << t << '\t';
        cout << fabs(ferro.calc_magn())/L/L << '\t';
        cout << fabs(ferro2.calc_magn())/L/L << '\n';
    }
}

int main(){
    hist();
}
