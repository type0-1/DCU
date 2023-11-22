#include <stdio.h>
#include <stdlib.h>

void allocate_memory(int**);
void assign_values(int*, char*[]);
void assign_more_values(int*, int*, char*[]);
void sort_list(int*, int*);
void get_frequent(int*, int*, int*, int*);
void add_frequent(int*, int*, int*, int*);
void print_values(int*, int*);

int main(int argc, char *argv[]){

    int *nums = NULL, size = 5;
    nums = (int*)calloc(5, sizeof(int));

    if(!nums){
        printf("Memory allocation failed, exiting...\n");
        exit(1);
    }

    assign_values(nums, argv);

    if(argc-1 > 5){
        size = 6;
        for(int i = size + 1; i < argc; ++i){
            printf("%d ---> %d\n", i, argc-1);
            printf("%d |---| %d\n", atoi(argv[i]), atoi(argv[i+1]));
            assign_more_values(nums, &i, argv);
        }
        size = argc-1;
    }

    print_values(nums, &size);

}

void assign_values(int *nums, char *argv[]){
    for(int i = 1; i < 6; ++i){
        *(nums + (i - 1)) = atoi(argv[i]);
    }
}

void assign_more_values(int *nums, int *size, char *argv[]){
    int *temp = (int*)calloc(*size + 1, sizeof(int));
    nums = temp;
    *(nums + *size + 1) = atoi(argv[*size]);
}
void print_values(int *nums, int *size){

    for(int i = 0; i < *size; ++i){
        printf("%d\n", *(nums + i));
    }
}
