#include<iostream>
#include<fstream>
#include<math.h>

#define T_FIN 100
#define dt 5e-2
#define v0 0
#define x0 2

using namespace std;
void euler_ohs(){
    ofstream ofile("ohs_euler.dat");
    double f, dE;
    double v = v0;
    double x = x0;
    double E0 = v*v/2 + x*x/2;
    for(double t=0; t<T_FIN; t+=dt){
        dE = (v*v/2 + x*x/2)/E0 - 1;
        f = -x;
        x += v * dt;
        v += f * dt;
        ofile << t << '\t';
        ofile << x << '\t';
        ofile << v << '\t';
        ofile << dE << '\n';
    }
    ofile.close();
}

void euler_cromer_ohs(){
    ofstream ofile("ohs_euler_cromer.dat");
    double f, dE;
    double v = v0;
    double x = x0;
    double E0 = v*v/2 + x*x/2;
    for(double t=0; t<T_FIN; t+=dt){
        dE = (v*v/2 + x*x/2)/E0 - 1;
        f = -x;
        v += f * dt;
        x += v * dt;
        ofile << t << '\t';
        ofile << x << '\t';
        ofile << v << '\t';
        ofile << dE << '\n';
    }
    ofile.close();
}

void velocity_verlet_ohs(){
    ofstream ofile("ohs_velocity_verlet.dat");
    double f, v, x, E0, dE;
    v = v0;
    x = x0;
    E0 = v*v/2 + x*x/2;
    dE = 0;
    for(double t=0; t<T_FIN; t+=dt){
        dE = (v*v/2 + x*x/2)/E0 - 1;
        v += -x * dt/2; // atualiza 1/2 velocidade (f = -x)
        x += v * dt;    // atualiza posicao
        v += -x * dt/2; // termina atualizacao velocidade
        ofile << t << '\t';
        ofile << x << '\t';
        ofile << v << '\t';
        ofile << dE << '\n';
    }
    ofile.close();
}

int main(){
    euler_ohs();
    euler_cromer_ohs();
    velocity_verlet_ohs();
}
