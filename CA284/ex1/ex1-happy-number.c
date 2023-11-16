#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void happy_num(int);
int sum(int);

int main(int argc, char *argv[]){
    
    happy_num(atoi(argv[1]));
    
    return 0;
}

void happy_num(int n){
    int limit = 0;
    while(n != 1){
        
        int temp = n;
        n = sum(temp);
        
        if(limit == 100){
            printf("not happy\n");
            return;
        }
        limit++;
    }
    
    printf("is happy\n");
}

int sum(int n){
    int total = 0;
    while(n != 0){
        total += (n%10)*(n%10);
        n/=10;
    }
    return total;
}