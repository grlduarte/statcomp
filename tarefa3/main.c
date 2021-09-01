#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define P 0.5
#define T_FINAL 500
//#define N_HIST 10000

int sorteia(){
    float unit_rnd = rand() / (float) RAND_MAX;
    if (unit_rnd > (1-P)){
        return +1;
    }
    else{
        return -1;
    }
}

int main(int argc, char *argv[]){
    int N_HIST;
    sscanf(argv[1], "%d", &N_HIST);

    srand(time(0));
    printf("%d\n", N_HIST);
    float x2[T_FINAL], x4[T_FINAL];
    int n, x, t;
    for(t=0; t<T_FINAL; t++)
        x2[t] = x4[t] = 0;

    n = 0;
    while (n < N_HIST){
        x = 0;
        for (t=0; t<T_FINAL; t++){
            x += sorteia();
            x2[t] += x*x;
            x4[t] += pow(x, 4);
        }
        n++;
    }
    
    double med_x2, med_x4, sigma;
    for (t=0; t<T_FINAL; t++){
        med_x2 = x2[t] / N_HIST;
        med_x4 = x4[t] / N_HIST;
        sigma = sqrt((med_x4 - pow(med_x2, 2)) / (N_HIST - 1));
        printf("%d\t%f\t%f\n", t, med_x2, sigma);
    }
}
