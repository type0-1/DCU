#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void odd_even(int, char**);
int odd(int, char**);
int even(int, char**);

int main(int argc, char *argv[]){
    
    if(argc == 2){
        if(atoi(argv[1]) % 2 == 0){
            printf("%d\n%d\n", 0, atoi(argv[1]));
        }
        else{
            printf("%d\n%d\n", atoi(argv[1]), 0);
        }
    }
    else{
        odd_even(argc-1, argv);
    }
    return 0;
}

void odd_even(int argc, char** argv){
    int oddN = odd(argc, argv);
    int evenN = even(argc, argv);
    printf("%d\n%d\n", oddN, evenN);
}

int odd(int argc, char **argv){
    
    int odds = 0;
    for(int i = 1; i < argc; ++i){
        if(atoi(argv[i]) % 2 != 0){
            odds+=atoi(argv[i]);
        }
    }
    
    return odds;
}

int even(int argc, char **argv){
    
    int i = 1, evens;
    
    while(atoi(argv[i]) % 2 != 0){
        i++;
    }
    
    evens = atoi(argv[i]);
    i+=1;
    
    for(i; i <= argc; ++i){
        if(atoi(argv[i]) % 2 == 0){
            evens-=atoi(argv[i]);
        }
    }
    return evens;
}