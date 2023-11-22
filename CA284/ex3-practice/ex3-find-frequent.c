#include <stdio.h>
#include <stdlib.h>

void assign_values(int*, char*[]);
void assign_more_values(int**, int*, int*, char*[]);
void sort_list(int*, int*);
void get_frequent(int*, int**, int*, int*);
void add_frequent(int**, int*, int*, int*, int*);
void print_frequent(int*, int*);

int main(int argc, char *argv[]){

    int *nums = NULL, size = 5;
    nums = (int*)calloc(5, sizeof(int));

    if(!nums){
        printf("Memory allocation failed, exiting...\n");
        exit(1);
    }

    assign_values(nums, argv);

    if(argc - 1 > 5){
        assign_more_values(&nums, &size, &argc, argv);
    }

    sort_list(nums, &size);

    int *frequent = NULL, frequent_size = 1;
    frequent = (int*)calloc(frequent_size, sizeof(int));

    if(!frequent){
        printf("Memory allocation failed, exiting...\n");
        exit(1);
    }

    get_frequent(nums, &frequent, &size, &frequent_size);

    print_frequent(frequent, &frequent_size);

    free(nums);
    free(frequent);

}

void assign_values(int *nums, char *argv[]){
    for(int i = 1; i < 6; ++i){
        nums[i-1] = atoi(argv[i]);
    }
}

void assign_more_values(int **nums, int *size, int *argc, char *argv[]){

    for(int i = 6; i < *argc; ++i){
        *size = *size + 1;
        int *temp = realloc(*nums, (*size)*sizeof(int));
        *nums = temp;
        (*nums)[*size - 1] = atoi(argv[*size]);
    }

}

void sort_list(int *nums, int *size){

    for(int i = 0; i < *size; ++i){
        for(int j = i + 1; j < *size; ++j){
            if(nums[i] > nums[j]){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
            }
        }
    }

}

void get_frequent(int *nums, int **frequent, int *size, int *frequent_size){

    int count = 0, prev = nums[0], index = 0;

    for(int i = 0; i < *size; ++i){
        if(prev == nums[i]){
            count++;
        }
        else{
            if(count > 3){
                add_frequent(frequent, &prev, &count, frequent_size, &index);
            }
            count = 1;
        }
        prev = nums[i];
    }

    if(count > 3){
        add_frequent(frequent, &prev, &count, frequent_size, &index);
    }
}

void add_frequent(int **frequent, int *prev, int *count, int *frequent_size, int *index){

    for(int i = 0; i < *count; ++i, *index += 1){
       *frequent_size += 1;
       int *temp = realloc(*frequent, (*frequent_size)*sizeof(int));
       *frequent = temp;
       (*frequent)[*index] = *prev;
    }

}

void print_frequent(int *frequent, int *frequent_size){
    for(int i = 0; i < *frequent_size - 1; ++i){
        printf("%d\n", frequent[i]);
    }
}