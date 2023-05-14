#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){
    int search = atoi(argv[1]);
    for (int i = 2; i < argc; ++i){
        if (search == atoi(argv[i])){
            printf("Found %d at %d\n", search, i - 2);
        }
    }
    return 0;
}