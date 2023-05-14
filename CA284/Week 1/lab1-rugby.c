#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){
    int try = atoi(argv[1]) * 5;
    int conver = atoi(argv[2]) * 2;
    int pen = atoi(argv[3]) * 3;
    int dg = atoi(argv[4]) * 3;

    printf("%d\n", (try + conver + pen + dg));
    return 0;

}