#include<stdio.h>
int findLRU(int time[], int n){
	int i, minimum = time[0], pos = 0;

	for(i = 1; i < n; ++i){
		if(time[i] < minimum){
			minimum = time[i];
			pos = i;
		}
	}

	return pos;
}

int main()
{
    int no_of_frames, no_of_pages, page_hits,frames[10], pages[30], counter = 0, time[10], flag1, flag2, i, j, pos, faults = 0;
	printf("\n------------------------------------------------------------------------------------------------\n");

	printf("\n Enter the number of pages : ");
	scanf("%d", &no_of_pages);

	printf("\n------------------------------------------------------------------------------------------------\n");

    printf("\n Enter the Values of the Reference String : \n");

    for(i = 0; i < no_of_pages; ++i)
    {
    	printf(" Value No. [%d] : ", i+ 1);
    	scanf("%d", &pages[i]);
    }
    printf("\n------------------------------------------------------------------------------------------------\n");

    printf("\n Enter the number of frames : ");
	scanf("%d", &no_of_frames);

	printf("\n------------------------------------------------------------------------------------------------\n");
	for(i = 0; i < no_of_frames; ++i){
    	frames[i] = -1;
    }
    for(i = 0; i < no_of_pages; ++i){
    	flag1 = flag2 = 0;
    	for(j = 0; j < no_of_frames; ++j){
    		if(frames[j] == pages[i]){
	    		counter++;
	    		time[j] = counter;
	   			flag1 = flag2 = 1;
	   			break;
   			}
    	}
    	if(flag1 == 0){
			for(j = 0; j < no_of_frames; ++j){
	    		if(frames[j] == -1){
	    			counter++;
	    			faults++;
	    			frames[j] = pages[i];
	    			time[j] = counter;
	    			flag2 = 1;
	    			break;
	    		}
    		}
    	}
    	if(flag2 == 0){
    		pos = findLRU(time, no_of_frames);
    		counter++;
    		faults++;
    		frames[pos] = pages[i];
    		time[pos] = counter;
    	}
    	printf("\n");
    	for(j = 0; j < no_of_frames; ++j){
    		printf(" %d\t", frames[j]);
    	}
	}
      page_hits =  no_of_pages - faults;
      printf("\n------------------------------------------------------------------------------------------------\n");
      printf("\n Total Page Hits : %d\n", page_hits);
      printf("\n Total Page Miss : %d\n", faults);

      printf("\n Page Hit Ratio : %f\n", (double)page_hits/no_of_pages);
      printf("\n Page Miss Ratio : %f\n",(double)faults/no_of_pages);

      printf("\n------------------------------------------------------------------------------------------------\n");
    return 0;
}
