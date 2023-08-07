#include <stdio.h>
#include <stdlib.h>


int subtractEven(int firstEven, int number){
    return firstEven - number;
}

int addOdd(int oddNum, int number){
    return oddNum + number;
}

int main(int argc, char*argv[]){
    int evenNum, oddNum, i, j;
    evenNum = 0;
    oddNum = 0;
    i = 1;
    j = 1;
    
    for(i; i < argc; ++i){
        if(atoi(argv[i]) % 2 == 0){
            evenNum = atoi(argv[i]);
            break;
        }
    }
    for(i=i+1; i < argc; ++i){
        if(atoi(argv[i]) % 2 == 0){
            evenNum = subtractEven(evenNum, atoi(argv[i]));
        }
    }
    
    for(j; j < argc; ++j){
        if(atoi(argv[j]) % 2 != 0){
            oddNum = atoi(argv[j]);
            break;
        }
    }
    
    for(j = j+1; j < argc; ++j){
        if(atoi(argv[j]) % 2 != 0){
            oddNum = addOdd(oddNum, atoi(argv[j]));
        }
    }
    
    printf("%d\n", oddNum);
    printf("%d\n", evenNum);
    return 0;
}