#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Country countries;

void assign_values(countries*, char*[], int);
void print_values(countries);

struct Country{
    char country[25];
    char city[25];
    int size;
    float pop;
};

int main(int argc, char *argv[]){
    
    printf("Country\t\t\tCapital\t\t\tSize\t\t\tPopulation\n");
    
    int size = (argc-1)/4;
    countries locations[size];
    int pos = 0;
    
    for(int i = 1; i < argc; i+=4){
        assign_values(&locations[pos], argv, i);
        pos++;
    }
    
    for(int i = 0; i < size; ++i){
        print_values(*(locations + i));
    }
    return 0;
}

void assign_values(countries *location, char* argv[], int i){
    
    countries *cInfo = location;
    
    strcpy(cInfo->country, argv[i]);
    strcpy(cInfo->city, argv[i+1]);
    cInfo->pop = atof(argv[i+2]);
    cInfo->size = atoi(argv[i+3]);
    
    
}

void print_values(countries location){
    
    printf("%s\t\t\t%s\t\t\t%d\t\t\t%.2f\n", location.country, location.city, location.size, location.pop);
    
}