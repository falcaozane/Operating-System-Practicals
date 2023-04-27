#include<stdio.h>
#include<stdlib.h>
#include<math.h>

int main(){
    int queue[30],n,head,i,j,k,seek=0,range,diff,temp,q1[30],q2[30],temp1=0,temp2=0;
    printf("SSTF algo: \n");
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
    queue[0]=head;
    printf("%d=>",queue[0]);
    // copy q2 contents to queue
    for( i = 1,j=0; j < temp2; i++,j++)
    {
        queue[i]=q2[j];
        printf("%d=>",queue[i]);
    }
    
    // copy q1 contents to queue
    for( i = temp2+2,j=0; j < temp1; i++,j++)
    {
        queue[i]=q1[j];
        printf("%d=>",queue[i]);
    }
    //queue[i]=range;
    //queue[0]=head;
}