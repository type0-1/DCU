#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){
    int largest = 0;
    
    for(int i = 0; i < argc; ++i){
        if(i == argc-1){
            if(largest <= atoi(argv[i])){
                largest = atoi(argv[i]);
                printf("%d\n", largest);
            }
            else{
                printf("%d\n", largest);
            }
        }
        else{
            if(largest <= atoi(argv[i])){
                largest = atoi(argv[i]);
            }
        }
    }
    return 0;
}