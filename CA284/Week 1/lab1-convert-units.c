#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){
    int units = atoi(argv[1]);
    printf("%.2f\n", units/2.54);
}