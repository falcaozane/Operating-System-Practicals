#include<stdio.h>
#include<sys/types.h>
#include<unistd.h>

void main(){
    int pid = fork();
    if (pid>0){
        sleep(80);
    }
    else{
        exit(0);
    }

}