#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void largeOrSmall(int, char**);
float largest(int, char**);
float smallest(int, char**);

int main(int argc, char *argv[]){
    largeOrSmall(argc-1, argv);
    return 0;
}

void largeOrSmall(int argc, char** argv){
    if(strcmp(argv[1], "largest") == 0){
        printf("%.2f\n", largest(argc, argv));
    }
    else{
        printf("%.2f\n", smallest(argc, argv));
    }
}

float largest(int argc, char **argv){
    float largest = atof(argv[2]);
    
    for(int i = 2; i < argc; ++i){
        if(largest < atof(argv[i])){
            largest = atof(argv[i]);
        }
    }
    
    return largest;
}

float smallest(int argc, char **argv){
    float smallest = atof(argv[2]);
    
    for(int i = 2; i < argc; ++i){
        if(smallest > atof(argv[i])){
            smallest = atof(argv[i]);
        }
    }
    
    return smallest;
}