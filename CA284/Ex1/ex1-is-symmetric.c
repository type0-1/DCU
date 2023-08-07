#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void getResult(int amount, char word[]){
    int check = 1;
    for(int i = 0; i < amount; ++i){
        if(word[i] != word[strlen(word) - i - 1]){
            check = 0;
        }
    }
    if (check == 1){
        printf("yes\n");
    }
    else{
        printf("no\n");
    }
}

int main(int argc, char*argv[]){
    getResult(strlen(argv[1]), argv[1]);
    return 0;
}