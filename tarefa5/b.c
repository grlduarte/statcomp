#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "rands.h"

#define N_HIST 1e6
#define XMIN 0.
#define XMAX 8.


int main(int argc, char *argv[]){
    int N_BINS;
    sscanf(argv[1], "%d", &N_BINS);
    int histograma[N_BINS];
    for(int i=0; i<N_BINS; i++) histograma[i] = 0;

    INIT_FRANDOM(seedinit());
    double x, y;
    double dx = (XMAX - XMIN) / N_BINS;
    int m = 0;

    for(int i=0; i<N_HIST; i++){
        x = XMAX * FRANDOM;
        y = FRANDOM;
        if(y < exp(-x)){
            for(int n=0; n<N_BINS; n++){
                if((x >= n*dx) && (x <= (n+1)*dx)) histograma[n]++;
            }
            m++;
        }
    }
    for(int n=0; n<N_BINS; n++)
        printf("%lf\t%lf\n", (n+0.5)*dx, histograma[n]/dx/m);
}
