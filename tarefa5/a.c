#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "rands.h"

#define N_HIST 1000
#define XMIN 0.
#define XMAX 10.

double ngaussian(void){
  static int iset=0;
  static double gset;
  double z,r,theta;
  
  if (iset==0) {
    theta=2.0*M_PI*FRANDOM;
    z = FRANDOM;
    r=sqrt(-2.0*log(1.0-z));
    gset=r*sin(theta);
    iset=1;
    return r*cos(theta);
  }
  else {
    iset=0;
    return gset;
  }
}

int main(int argc, char *argv[]){
    int N_BINS;
    sscanf(argv[1], "%d", &N_BINS);
    int histograma[N_BINS];
    for(int i=0; i<N_BINS; i++) histograma[i] = 0;

    INIT_FRANDOM(seedinit());
    double dx = (XMAX - XMIN) / N_BINS;
    double x;

    for(int i=0; i<N_HIST; i++){
        x = 5. + 2.*ngaussian();
        for(int n=0; n<N_BINS; n++){
            if((x >= n*dx) && (x <= (n+1)*dx)) histograma[n]++;
        }
    }
    for(int n=0; n<N_BINS; n++)
        printf("%lf\t%lf\n", (n+0.5)*dx, histograma[n]/dx/N_HIST);
}
