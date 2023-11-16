#include <stdio.h>
#include <stdlib.h>

void allocate(int*, int*, int*);

int main(int argc, char *argv[]){

    int *pVec1 = NULL, *pVec2 = NULL;
    int size = atoi(argv[1]);

    allocate(pVec1, pVec2, &size);

    if(!pVec1){
        printf("Unsuccessful memory allocation, exiting...\n");
        return 0;
    }

    return 0;
}

void allocate(int *pVec1, int *pVec2, int *size){

    pVec1 = calloc(*size, sizeof(int));
    pVec2 = calloc(*size, sizeof(int));
}

