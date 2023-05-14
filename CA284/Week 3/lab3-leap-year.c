#include <stdio.h>
#include <stdlib.h>

void getLeap(int start, int end){
    for(start; start <= end; ++start){
        if(start % 100 == 0){
            if(start % 400 == 0){
                printf("%d\n", start);
            }
        }
        else if(start % 4 == 0 && start % 100 != 0){
            printf("%d\n", start);
        }
    }
}
int main(int argc, char*argv[]){
    getLeap(atoi(argv[1]), atoi(argv[2]));
    return 0;
}