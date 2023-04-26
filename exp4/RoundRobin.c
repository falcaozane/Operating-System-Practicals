#include<stdio.h>  
  
int main()  
{  
	int i, no_of_processes , sum=0,count=0, y, quant, wt=0, tat=0, at[10], bt[10], temp[10];  
	float avg_wt, avg_tat;  
	
	printf("\n------------------------------------------------------------------------------------------------\n");
	printf("\n Enter the total number of process in the system : ");  
	scanf("%d", &no_of_processes);  
	printf("\n------------------------------------------------------------------------------------------------\n");
	
	y = no_of_processes ; // Assign the number of process to variable y  

	// Using for loop to enter the details of the process like Arrival time and the Burst Time  
	for(i=0; i < no_of_processes ; i++)  
	{  
		printf("\n Enter the Arrival and Burst time of the Process[%d]\n", i+1);  
		printf(" Arrival time : ");  // Accept arrival time  
		scanf("%d", &at[i]);  
		printf(" Burst time : "); // Accept the Burst time  
		scanf("%d", &bt[i]); 
		printf("\n------------------------------------------------------------------------------------------------\n");
		temp[i] = bt[i]; // store the burst time in temp array  
	}  
	// Accept the Time quantum  
	printf("\n Enter the Time Quantum for the process (in ms) : ");  
	scanf("%d", &quant);  
	printf("\n------------------------------------------------------------------------------------------------\n");
	
	// Display the process No, burst time, Turn Around Time and the waiting time  
	printf("\n Process No \t\t Burst Time \t\t Turnaround Time \t\t Waiting Time ");  
	for(i = 0; y!=0; )  
	{  
		if(temp[i] <= quant && temp[i] > 0) // defining the conditions   
		{  
			sum = sum + temp[i];  
			temp[i] = 0;  
			count=1;  
		}     
		else if(temp[i] > 0)  
		{  
			temp[i] = temp[i] - quant;  
			sum = sum + quant;    
		}  
		if(temp[i]==0 && count==1)  
		{  
			y--; //decrement the process no.  
			printf("\n Process[%d] \t\t  %d \t\t\t  %d \t\t\t\t %d", i+1, bt[i], sum-at[i], sum-at[i]-bt[i]);  
			wt = wt + sum - at[i] - bt[i];  
			tat = tat + sum - at[i];  
			count = 0;     
		}  
		if(i == no_of_processes-1)  
		{  
			i=0;  
		}  
		else if(at[i+1] <= sum)  
		{  
			i++;  
		}  
		else  
		{  
			i=0;  
		}  
	}  
	printf("\n------------------------------------------------------------------------------------------------\n");
	
	// Calculating the Average Waiting Time and Average Turnaround Time  
	avg_wt = wt * 1.0 / no_of_processes ;  
	avg_tat = tat * 1.0 / no_of_processes ;  
	
	printf("\n Average Turn Around Time : %f ms", avg_wt);  
	printf("\n Average Waiting Time : %f ms\n", avg_tat); 
	
	printf("\n------------------------------------------------------------------------------------------------\n");
	 
	return 0;  
}  