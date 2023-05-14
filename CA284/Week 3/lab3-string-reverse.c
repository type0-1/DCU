#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char*argv[]){
    for(int i = strlen(argv[1]) - 1; i >= 0; --i){
        printf("%c", argv[1][i]);
    }    
    printf("\n");
    return 0;
}