//#define DEBUG
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>
#include "rands.h"

#define N 1e9
double xx;

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

double ngaussian_boxm_nr(void){
  static int iset=0;
  static double gset;
  double fac,r,v1,v2;
  
  if (iset==0) {
    do {
      v1=2.0*FRANDOM-1.0;
      v2=2.0*FRANDOM-1.0;
      r=v1*v1+v2*v2;
    } 
    while (r>=1 || r==0.0);
    fac=sqrt(-2.0*log(r)/r);
    gset=v1*fac;
    iset=1;
    return v2*fac;
  }
  else {
    iset=0;
    return gset;
  }
}

double ngaussian_leva_nr(){
  double u,v,x,y,q;
  do {
    u = FRANDOM;
    v = 1.7156*(FRANDOM-0.5);
    x = u - 0.449871;
    y = fabs(v) + 0.386595;
    q = x*x + y*(0.19600*y-0.25472*x);
  } while (q > 0.27597 && (q > 0.27846 || v*v > -4.*log(u)*u*u));
  return v/u;
}


int main(){
  unsigned long i;
  
  INIT_FRANDOM(seedinit());

  for(i=0;i<N;i++){
    //xx = ngaussian_leva_nr();
    xx = ngaussian();
    //printf("%.14f\n",xx);
  }
    

  return 0;
}
