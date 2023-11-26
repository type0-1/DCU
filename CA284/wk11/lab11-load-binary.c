#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Student student;

void assign_values(student*, FILE*);

struct Student{
    char name[25];
    char college[25];
    int age;
    float grade;
};

int main(int argc, char *argv[]){
    char *filename = "studentBinary.bin";

    int name_length, college_length;

    FILE *rfile = fopen(filename, "rb");

    student *person = (student*)calloc(1, sizeof(student));
    
    if(!rfile){
        printf("Error occured.\n");
        exit(1);
    }   

    fread(&name_length, sizeof(int), 1, rfile);
    fread(person->name, sizeof(char), name_length, rfile);
    fread(&college_length, sizeof(int), 1, rfile);
    fread(person->college, sizeof(char), college_length, rfile);
    fread(&person->age, sizeof(int), 1, rfile);
    fread(&person->grade, sizeof(float), 1, rfile);

    printf("Name: %s\nCollege: %s\nAge: %d\nGrade: %.2f\n", person->name, person->college, person->age, person->grade);

    return 0;
}
