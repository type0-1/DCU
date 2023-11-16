#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void triangular(int);


int main(int argc, char *argv[]){
    
    triangular(atoi(argv[1]));
    
    return 0;
}

void triangular(int n){
    int increment = 1;
    for(int i = 1; i < n*n; i+=increment){
        if(i == n){
            printf("%d is a triangular number\n", n);
            return;
        }
        else if(i > n){
            printf("%d is not a triangular number\n", n);
            return;
        }
        increment++;
    }
}
