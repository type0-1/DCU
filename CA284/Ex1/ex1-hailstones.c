#include <stdio.h>
#include <stdlib.h>

void hailstone(int number){
    printf("%d ", number);
    while(number != 1){
        if (number % 2){
            number = (3*(number)) + 1;
        }
        else if (number % 2 == 0){
            number = number / 2;
        }
        if(number != 1){
            printf("%d ", number);
        }
    }
    printf("%d", number);
    printf("\n");
}

int main(int argc, char*argv[]){
    hailstone(atoi(argv[1]));
    return 0;
}