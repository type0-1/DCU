#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void symmetric(char*);


int main(int argc, char *argv[]){
    
    symmetric(argv[1]);
    
    return 0;
}

void symmetric(char *string){
    int i = 0;
    while(string[i] == string[strlen(string) - i - 1]){
        i++;
    }
    i-1 == strlen(string) ? printf("yes\n") : printf("no\n");
}
