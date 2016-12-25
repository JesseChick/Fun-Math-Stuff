#include <stdlib.h>
#include <stdio.h>
#include <math.h>

double generateK0(int);
double generateK0_Recursively(double,int,int);

int* continuedFractionExpansion(double,int);

void freeMemory(void*);

int main() {
  const int MAX_TERM = 5000;

  // printf("iter: %f\n", generateK0(MAX_TERM));
  // printf("rec:  %f\n", generateK0_Recursively(1, 1, MAX_TERM));

  double phi = (1 + pow(5.0,0.5)) / 2;
  int* cf = continuedFractionExpansion(3.14, 5);


  freeMemory(cf);

  return 0;
}

double generateK0(int max_term) {
  double k0 = 1;
  for (int r=1; r<=max_term; r++) {
    k0 *= pow(
            1 + (1.0 / (r*(r+2))),
            log2(r)
          );
  }
  return k0;
};
double generateK0_Recursively(double k0, int r, int max_term) {
  if (r > max_term) return k0;
  else return k0 * generateK0_Recursively( pow(
                                              1 + (1.0 / (r*(r+2))),
                                              log2(r)
                                            ),
                                            r + 1,
                                            max_term);
};

int* continuedFractionExpansion(double number, int max_n) {
  int* a = malloc((max_n) * sizeof(int));

  // printf("CFE of %f: ", number);
  for (int n=1; n<=max_n; n++) {
    a[n] = (int)number;
    printf("%f ", number);
    number = 1.0 / (double)(number - a[n]);
    // printf("%d ", a[n]);
  }
  // printf("\n");

  return a;
};

void freeMemory(void* ptr) {
  free(ptr);
};
