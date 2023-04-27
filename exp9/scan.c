#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int absoluteVal(int x){
    if (x>0) return x;
    else return x*-1;
}
void main(){
    int queue[30],n,head,i,j,k,seek=0,range,diff,temp,q1[20],q2[20],temp1=0,temp2=0;
    printf("SCAN algo: \n");
    printf("Enter max range of disk: ");
    scanf("%d",&range);
    printf("\nEnter no. of queue request: ");
    scanf("%d",&n);
    printf("\nEnter initial head position: ");
    scanf("%d",&head);
    printf("Enter queue sequence: ");
    for ( i = 1; i <=n; i++)
    {
        scanf("%d",&temp);
        if(temp>head){
            q1[temp1] = temp;
            temp1++;
        }
        else{
            q2[temp2] = temp;
            temp2++;
        }
    }
    // sorting in ascending order
    for(i=0;i<temp1-1;i++){
        for(j=i+1;j<temp1;j++){
            if(q1[i]>q1[j]){
                temp = q1[i];
                q1[i] = q1[j];
                q1[j] = temp;
            }
        }
    }
    // sorting in descending order
    for(i=0;i<temp2-1;i++){
        for(j=i+1;j<temp2;j++){
            if(q2[i]<q2[j]){
                temp = q2[i];
                q2[i] = q2[j];
                q2[i]=temp;
            }
        }
    }
    // copy q1 contents to queue
    for( i = 1,j=0; j < temp1; i++,j++)
    {
        queue[i]=q1[j];
    }
    queue[i]=range;
    // copy q2 contents to queue
    for( i = temp1+2,j=0; j < temp2; i++,j++)
    {
        queue[i]=q2[j];
    }
    queue[i]=0;
    queue[0]=head;
    for (j = 0; j <=n; j++)
    {
        diff = absoluteVal(queue[j+1]-queue[j]);
        seek+=diff;
        printf("\n Disk moves from %d => %d with seek time: %d \n",queue[j],queue[j+1],diff);
    }
    
}