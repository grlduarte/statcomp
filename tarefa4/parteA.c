#include <stdio.h>
#include <stdlib.h>
#include <time.h>

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
    int N;
    sscanf(argv[1], "%d", &N);
    int T_FINAL = N * 5;
    int flea[N];
    for (int i=0; i<N; i++) flea[i] = 0;
    int ind, t=0;
    srand(time(0));

    while (t<T_FINAL){
        ind = sorteia() * N;
        flea[ind] = (flea[ind] + 1) % 2;
        printf("%f\t%f\n", (float) t/N, (float) soma_vetor(flea, N)/N);
        t++;
    }
}
