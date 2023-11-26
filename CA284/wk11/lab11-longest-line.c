#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
    FILE *rfile = NULL;
    char *filename = "paragraph.txt";
    rfile = fopen(filename, "r");

    if(!rfile){
        printf("Error occured\n");
        exit(1);
    }

    int size = 1, i = 0, end = 0, count = 0, largest = 0, mchar = fgetc(rfile);

    while(mchar != EOF){
        size++;
        mchar = fgetc(rfile);
    }
    
    char *text = (char*)calloc(size, sizeof(char));

    rfile = fopen(filename, "r");

    mchar = fgetc(rfile);

    while(mchar != EOF){
        *(text + i) = mchar-'\0';
        i++;
        mchar = fgetc(rfile);
    }

    i = 0;

    for(; i < size; ++i){
        if(*(text + i) == '.'){
            if(count > largest){
                end = i;
                largest = count;
            }
            count = 0;
        }
        count++;
    }

    i = end - 1;

    while(!('A' <= *(text + i) && *(text + i) <= 'Z')){
        i--;
    }

    printf("%d\n", largest);

    while(*(text + i - 1) != *(text + end)){
        printf("%c", *(text + i));
        i++;
    }

    printf("\n\n");

    free(text);

    return 0;
}