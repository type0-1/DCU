#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void assign_string(char**, char*);
void check_absence(char*, int*, int*);
void check_late(char*, int*, int*);

int main(int argc, char *argv[]){

    int status = 0, a_count = 0, l_count = 0;

    for(int i = 1; i < argc; ++i){

        char *string = NULL;

        assign_string(&string, *(argv + i));

        if(!string){
            printf("Error occured in memory allocation...\n");
            exit(1);
        }

        check_absence(string, &a_count, &status);

        if(status){
            printf("%d\n", status);
            status = 0;
            continue;
        }

        check_late(string, &l_count, &status);

        if(status){
            printf("%d\n", status);
            status = 0;
            continue;
        }
        else{
            printf("%d\n", status);
        }


        free(string);

    }

    return 0;
}

void assign_string(char **string, char *string_2){

    *string = calloc(strlen(string_2), sizeof(char));
    strcpy(*string, string_2);
    
}

void check_absence(char *string, int *a_count, int *status){

    for(int i = 0; i < strlen(string); ++i){
        if(*(string + i) == 'A'){
           *a_count += 1;
        }
    }
    
    if(*a_count >= 3){
        *status = 1;
    }

    *a_count = 0;

}

void check_late(char *string, int *l_count, int *status){

    for(int i = 0; i < strlen(string); ++i){

        if(*(string + i) == 'L'){

            while(*(string + i) == 'L'){
                *l_count += 1;
                i++;
            }

            if(*l_count >= 3){
                *status = 1;
                return;
            }
        }

        *l_count = 0;

    }

}