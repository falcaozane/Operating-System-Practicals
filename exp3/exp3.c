#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>
#define BUFFER_SIZE 1024
int main()
{
    int source_file, destination_file, n;
    char buffer[BUFFER_SIZE];
    source_file = open("file.txt", O_RDONLY); // Opening Source File
    if (source_file == -1)
    {
        printf("Unable to open source file.");
        exit(1);
    }
    // Opening Destination File Or Creating it
    destination_file = open("new.txt", O_WRONLY | O_CREAT, 0644);
    if (destination_file == -1)
    {
        printf("Unable to open destination file.");
        exit(1);
    }
    while ((n = read(source_file, buffer, BUFFER_SIZE)) > 0) //Copying the contents 
    {
        if (write(destination_file, buffer, n) != n)
        {
            printf("Error writing to destination file.");
            exit(1);
        }
    }
    close(source_file);// Close both files
    close(destination_file);
    // Open the destination file in read-only mode
    destination_file = open("new.txt", O_RDONLY);
    if (destination_file == -1)
    {
        printf("Unable to open destination file.");
        exit(1);
    }
    // Display the contents of the destination file
    while ((n = read(destination_file, buffer, BUFFER_SIZE)) > 0)
    {
        if (write(STDOUT_FILENO, buffer, n) != n)
        {
            printf("Error writing to standard output.");
            exit(1);
        }
    }
    close(destination_file);
    return 0;
}