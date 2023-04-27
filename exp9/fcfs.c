#include<stdio.h>
#include<stdlib.h>
#include<math.h>

void main(){

    int queue[20],n,head,i,j,k,seek=0,max,diff;
    printf("FCFS disk secdhuling algo\n");
    printf("Enter maximum range of disk: ");
    scanf("%d",&max);
    printf("Enter maxium no. of queue request: ");
    scanf("%d",&n);
    printf("Enter sequence: ");
    for(i=1;i<=n;i++){
        scanf("%d",&queue[i]);
    }
    printf("Initial head position: ");
    scanf("%d",&head);
    queue[0]=head;
    for( j = 0; j <= n-1; j++)
    {
        diff = abs(queue[j+1]-queue[j]);
        seek+=diff;
        printf("\n%d => %d in sek time: %d \n",queue[j],queue[j+1],diff);
    }
    printf("\nTotal head movements: %d",seek);
    
}