#include<stdio.h>
#include<stdlib.h>

void main()
{
    int n;
    printf("Enter the number of requests\n");
    scanf("%d",&n);
    
    int r[n];
    printf("Enter the requests one by one\n");
    for(int i=1; i<=n; i++)
    {
        scanf("%d",&r[i]);
    }
    
    int h;
    printf("Enter the head position\n");
    scanf("%d",&h);
    
    
    int arr1[100];
    int arr2[100];
    int count1=0,count2=0;
    for(int i=1; i<=n; i++)
    {
        if(h<=r[i])
        {
            count1=i-1;
            count2=i;
            break;
        }
    }
    int k=1;
    for(int i=count1; i>=1; i--)
    {
       arr1[k]=r[i];
       printf("%d\t",arr1[k]);
       k++;
    }
    
    for(int i=1; i<=count1; i++)
    {
       r[i]=arr1[i];
    }
    
    printf("\nr array\n");
    for(int i=1; i<=n; i++)
    {
        printf("%d\t",r[i]);
    }
    
    printf("Sequence is: %d",h);
    for(int i=1; i<=n; i++)
    {
        printf("->%d",r[i]);
    }
    
    int soln[n];
    for(int i=1; i<=n; i++)
    {
        if(i==1)
        {
            soln[i]=abs(h-r[i]);
        }
        else 
        {
            soln[i]=abs(r[i]-r[i-1]);
        }
        
    }
    
     printf("\nSoln array is\n");
    for(int i=1; i<=n; i++)
    {
        printf("%d\t",soln[i]);
    }
    
    int st=0;
    for(int i=1; i<=n; i++)
    {
        st=st+soln[i];
    }
    printf("\nSeek time is: %d",st);
}