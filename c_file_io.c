#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *fptr;
    char filename[] = "example_file.txt";
    char ch;

    fptr = fopen(filename, "w");
    if (fptr == NULL) {
        printf("Error opening file!\n");
        exit(1);
    }

    fprintf(fptr, "This is some text written to the file.\n");
    fclose(fptr);

    printf("File written successfully.\n");
    return 0;
}