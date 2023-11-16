#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void hailstone(int);


int main(int argc, char *argv[]){
    
    hailstone(atoi(argv[1]));
    
    return 0;
}

void hailstone(int n){
    while(n != 1){
        printf("%d ", n);
        n = n % 2 == 0 ? n/2 : 3*(n)+1;
    }
    
    printf("%d\n", n);
}
