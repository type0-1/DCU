#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){
    double PI = 3.1415;
    double radius = atoi(argv[1]);
    double height = atoi(argv[2]);
    
    if (argc == 1){
        printf("No input given!");
    }
    else if(argc == 2){
        printf("Two arguments needed!");
    }
    else if ((radius < 0 || height < 0)){
        printf("The radius or height cannot be negative!");
    }
    else{
        double area = ((2*(PI))*(radius)*(height)) + ((2*(PI))*(radius * radius));
        printf("%.2f", area);
    }
    printf("%d", argc);
}