#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float sum(float, float);
float difference(float, float);
float product(float, float);
float division(float, float);
float power(float, float);
float natural_log(float, float);

int main(int argc, char *argv[]){
	
	float a = atof(argv[1]);
	float b = atof(argv[2]);
	float (*pFunction)(float, float);
	
	float (*functions[6])(float, float) = {sum, difference, product, division, power, natural_log};
	for(int i = 0; i < 6; ++i){
		pFunction = functions[i];
		printf("%.2f\n", pFunction(a, b));
	}

	return 0;
}

float sum(float a, float b){
    return a + b;
}

float difference(float a, float b){
    return a - b;
}

float product(float a, float b){
    return a * b;
}

float division(float a, float b){
    return a / b;
}

float power(float a, float b){
	float result = pow(a,b);
    return result;
}

float natural_log(float a, float b){
	float result = log(a) + log(b);
    return result;
}