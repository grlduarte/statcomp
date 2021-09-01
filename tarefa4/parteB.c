#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

float sorteia(){
    float unit_rnd = rand() / (float) RAND_MAX;
    return unit_rnd;
}

int soma_vetor(int *flea_, int size){
    int i, soma=0;
    for(i=0; i<size; i++) soma += flea_[i];
    return soma;
}

int main(int argc, char *argv[]){
    int N=5000;
    int dt;
    sscanf(argv[1], "%d", &dt);
    int T_TRANS = 10 * N;
    int flea[N];
    for (int i=0; i<N; i++) flea[i] = 0;
    int ind, t=0;
    srand(time(0));

    while (t<T_TRANS){
        ind = sorteia() * N;
        flea[ind] = (flea[ind] + 1) % 2;
        t++;
    }

    double soma, med=0, med2=0;
    int Ns = 100;
    t=0;

    while (t<Ns){
        for(int i=0; i<dt; i++){
            ind = sorteia() * N;
            flea[ind] = (flea[ind] + 1) % 2;
        }
        soma = (double) soma_vetor(flea, N) / N;
        med += soma;
        med2 += pow(soma, 2);
        t++;
    }
    printf("%d\t%f\t%f\n", dt, (float) med/Ns, (float) sqrt( (med2/Ns - pow(med/Ns, 2)) / (Ns - 1) ));
}
