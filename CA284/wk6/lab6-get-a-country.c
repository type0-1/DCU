#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Country places;

void assign_values(places*, char*[]);
void print_values(places*);

struct Country{
	char country[25];
	char city[25];
	float size;
	int pop;
};

int main(int argc, char *argv[]){

	places location;

	assign_values(&location, argv);
	print_values(&location);

	return 0;
}

void assign_values(places *location, char *argv[]){

	places *cInfo;
	cInfo = location;
	
	strcpy(cInfo->country, argv[1]);
	strcpy(cInfo->city, argv[2]);
	cInfo->size = atof(argv[3]);
	cInfo->pop = atoi(argv[4]);

}

void print_values(places *location){
    
    places *cInfo = location;
    
    printf("%s\n%s\n%.2f million people\n%d km2\n", cInfo->country, cInfo->city, cInfo->size, cInfo->pop);
    
}