#include <stdio.h>
#include <stdlib.h>

void getTriangular(int number){
    int start = 1;
    int i = 2;
    while (start <= number){
        if (start == number){
            printf("%d is a triangular number\n", start);
            break;
        }
        start += i;
        ++i;
    }
    if (start > number){
        printf("%d is not a triangular number\n", number);
    }
}


int main(int argc, char*argv[]){
    getTriangular(atoi(argv[1]));
    return 0;
}