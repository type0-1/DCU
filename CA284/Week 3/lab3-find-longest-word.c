#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int findLongest(char word[]){
    int count = 0;
    int longest = 0;
    int position = 0;
    
    for(int i = 0; i <= strlen(word); ++i){
        if((word[i] != ' ' && word[i] != '\0')){
            ++count;
        }
        else{
            if (count >= longest){
                longest = count;
                position = i - longest;
                count = 0;
            }
            else{
                count = 0;
            }
        }
    }
    return position;
}

void printLongest(char word[], int start){
    while ((word[start] != '\0')){
        if ((word[start] == ' ')){
            break;
        }
        printf("%c", word[start]);
        ++start;
    }
    printf("\n");
}
int main(int argc, char*argv[]){
    int position = findLongest(argv[1]);
    printLongest(argv[1], position);
    return 0;
}