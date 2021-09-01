#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

float p = 0.5;

int sorteia(){
    float unit_rnd = rand() / (float) RAND_MAX;
    if (unit_rnd > (1-p)){
        return 1;
    }
    else{
        return 0;
    }
}

int sorteia_N(int N){
    int i = 0;
    int soma = 0;
    while (i < N){
        soma += sorteia();
        i++;
    }
    return soma;
}

int main(int argc, char *argv[]){
    int N_SORT, N_HIST;
    if (argc == 1){
        N_SORT = 5;
        N_HIST = 5e3;
    }
    else if(argc == 2){
        sscanf(argv[1], "%d", &N_SORT);
        N_HIST = 5e4;
    }
    else if(argc == 3){
        sscanf(argv[1], "%d", &N_SORT);
        sscanf(argv[2], "%d", &N_HIST);
    }
    else{
        printf("Too many arguments!\n");
    }

    srand(time(0));
    int hist[N_SORT+1];
    int i;
    for(i=0; i<N_SORT+1; i++)
        hist[i] = 0;

    int n = 0;
    while (n < N_HIST){
        hist[sorteia_N(N_SORT)]++;
        n++;
    }

    for(i=0; i<N_SORT+1; i++)
        printf("%d\t", hist[i]);
    printf("%d\n", N_HIST);
}
