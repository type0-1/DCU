#include <stdio.h>
#include <stdlib.h>
#include <string.h>

float getMulti(float num1, float num2){
    return num1 * num2;
}

float getDivide(float num1, float num2){
    return num1 / num2;
}

int main(int argc, char*argv[]){
    char* word = argv[1];
    float num1 = atof(argv[2]);
    float num2 = atof(argv[3]);
    
    if ((num1 == 0.0 || num2 == 0.0)){
        printf("invalid\n");
    }
    else{
        if (strcmp(word, "multiply") == 0){
            float result = getMulti(num1, num2);
            printf("%f\n", result);
        }
        else if(strcmp(word, "divide") == 0){
            float result2 = getDivide(num1, num2);
            printf("%f\n", result2);
        }
    }
    return 0;
}
