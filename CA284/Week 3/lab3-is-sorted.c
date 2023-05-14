#include <stdio.h>
#include <stdlib.h>

int main(int argc, char*argv[]){
    int grades[argc];
    int count = 0;
    for (int i = argc - 1; i > 0; --i){
        grades[count] = atoi(argv[i]);
        ++count;
    }
    for(int i = 0; i < argc - 1; ++i){
        for (int j = 0; j < argc - 1; ++j){
            if(grades[i] < grades[j]){
                int tmp = grades[i];
                grades[i] = grades[j];
                grades[j] = tmp;
            }
        }
    }
    for(int i = 0; i < argc - 1; ++i){
        printf("%d\n", grades[i]);
    }
    return 0;
}