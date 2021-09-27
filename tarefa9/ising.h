#include<vector>
#include<math.h>
#include<stdlib.h>
#include<time.h>

float ranf(){
    return rand() / (float) (RAND_MAX);
}

using namespace std;
class Ising2D{
        int L, N;
        int t_mcs;
        float T, h=0;
        vector<int> lattice;
        vector<int*> up, down, left, right;
        void init(size_t, float);
        void set_addresses();
        int flip_spin(int);
    public:
        Ising2D(size_t, float);
        void set_initial(int);
        void set_ext_field(float field){h = field;};
        void set_temperature(float T_){T = T_;};
        float temp(){return T;};
        double calc_energy();
        double calc_magn();
        int mc_step();
        void print();
};

Ising2D::Ising2D(size_t l, float _T=2.){
    /*
     *  Inicializa a matriz que contem os spins e 
     *  salva os parâmetros de entrada para o objeto.
     *  Por padrão a condição inicial é ferromagnética
     *  com todos spins = +1. Para a condição paramagnética
     *  use Ising2D::set_initial_para(0).
     */
    L = l;
    N = l*l;
    T = _T;
    t_mcs = 0;
    srand(time(0));
    lattice.resize(N, 1);
    up.resize(N);
    down.resize(N);
    left.resize(N);
    right.resize(N);
    set_addresses();
}

void Ising2D::set_addresses(){
    /*
     *  Salva o endereço dos vizinhos de cada spin.
     */
    int* i_0 = lattice.data(); // &lattice[0]
    for(int i=0; i<N; i++){
        int y = i%L;
        int x = (i - i%L)/L;
        int i_u = y + L * ((x+L-1)%L);
        int i_d = y + L * ((x+1)%L);
        int i_l = (y+L-1)%L + L*x;
        int i_r = (y+1)%L + L*x;
        up[i] = i_0 + i_u;
        down[i] = i_0 + i_d;
        left[i] = i_0 + i_l;
        right[i] = i_0 + i_r;
    }
}

void Ising2D::set_initial(int spin=+1){
    /*
     *  Configura a rede em uma condição inicial:
     *      * -1: ferromagnética com spins=-1;
     *      *  0: paramagnética com spins aleatórios;
     *      * +1: ferromagnética com spins=+1.
     */
    t_mcs = 0;
    if(abs(spin) == 1){
        for(int i=0; i<N; i++)
            lattice[i] = spin;
    }
    else if(spin == 0){
        for(int i=0; i<N; i++){
            if(ranf() > 0.5) lattice[i] = +1;
            else lattice[i] = -1;
        }
    }
    else return;
}

void Ising2D::print(){
    /*
     *  Imprime a rede formatada contanto que L < 10.
     */
    char sgn;
    if(L > 10) return;
    for(int i=0; i<N; i++){
        if(lattice[i] == 1) sgn = '+';
        else sgn = '-';
        cout << sgn << '\t';
        if((i+1)%L == 0) cout << '\n';
    }
}

double Ising2D::calc_energy(){
    /*
     *  Calcula e retorna a energia total (não normalizada)
     *  da rede.
     */
    float sum = 0;
    for(int i=0; i<N; i++){
        float neighbors = (*down[i] + *right[i]);
        sum += lattice[i] * neighbors;
    }
    return -sum;
}

double Ising2D::calc_magn(){
    /*
     *  Calcula e retorna a magnetização total (não normalizada
     *  e não módulo) da rede.
     */
    float sum = 0;
    for(int i=0; i<N; i++)
        sum += lattice[i];
    return sum;
}

int Ising2D::flip_spin(int i){
    /*
     *  Verifica se o spin escolhido satisfaz as condições
     *  e caso positivo alterna o sinal e retorna 1.
     *  Se não satisfaz as condições, retorna 0.
     */
    float d_energy = 2. * lattice[i] * (*up[i] + *down[i] + *left[i] + *right[i] + h);
    if((d_energy <= 0.) || (ranf() < exp(-d_energy/T))){
        lattice[i] *= -1;
        return 1;
    }
    else return 0;
}

int Ising2D::mc_step(){
    /*
     * Alterna N spins aleatórios se as condições são satisfeitas.
     * Retorna o tempo atual do sistema em Monte Carlo Steps.
     */
    for(int k=0; k<N; k++){
        int i = floor(ranf() * N);
        if(i>=N) i=0; // por algum motivo (talvez arredondamento) ranf -> [0,1]
        flip_spin(i);
    }
    return t_mcs++;
}
