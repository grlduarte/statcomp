#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

float p = 0.5;
float stop_par = 1e-3;

int sorteia(){
    float unit_rnd = rand() / (float) RAND_MAX;
    if (unit_rnd > (1-p)){
        return 1;
    }
    else{
        return 0;
    }
}

int main(){
    float soma_k, epsilon, med, med_now, stdev;
    soma_k = 0;
    med = 0;
    srand(time(0));

    int i = 1;
    while((epsilon > stop_par) | (i<100)){
        soma_k += sorteia();
        med_now = soma_k/i;
        epsilon = fabs(med_now - med);
        med = med_now;
        stdev = sqrt((med - pow(med, 2)) / (i-1));
        printf("%d\t%f\t%f\n", i, med, stdev);
        i++;
    }
}
