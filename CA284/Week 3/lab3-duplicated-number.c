#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){
    int grades[argc];
    int found = -1;
    int done = 0;
    for (int i = 0; i < argc; ++i){
        int search = atoi(argv[i]);
        int count = 0;
        for (int j = 0; j < argc; ++ j){
            if ((search == atoi(argv[j]) && done <= 2)){
                ++count;
                ++done;
                
            }
            if (count == 2){
                found = search;
            }
        }
    }
    if (found < 0){
        printf("no duplicated number\n");
    }
    else{
         printf("%d\n", found);   
    }
    return 0;
}