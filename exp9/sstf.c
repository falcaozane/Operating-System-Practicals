#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int main()
{
    int n, head_pos, seek_length = 0, disk_size;
    printf("Enter the size of the disk: ");
    scanf("%d", &disk_size);
    printf("Enter number of requests: ");
    scanf("%d", &n);
    int requests[n], done[n];
    printf("Enter the requests:");
    for (int i = 0; i < n; i++)
    {
        done[i] = 0;
        scanf("%d", &requests[i]);
    }
    printf("Enter the head position: ");
    scanf("%d", &head_pos);
    printf("Sequence: %d -> ", head_pos);
    for (int count = 0; count < n; count++)
    {
        int min_dist = disk_size + 1, min_idx = 0;
        for (int j = 0; j < n; j++)
        {
            if (done[j] == 0)
            {
                int dist = abs(requests[j] - head_pos);
                if (dist < min_dist)
                {
                    min_dist = dist;
                    min_idx = j;
                }
            }
        }
        done[min_idx] = 1;
        seek_length += min_dist;
        head_pos = requests[min_idx];
        printf("%d => ", requests[min_idx]);
    }
    printf("\nTotal seek length: %d\n", seek_length);
    return 0;
}