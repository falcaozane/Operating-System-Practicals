def round_robin(processes,AT,BT):
    count=0
    i=0
    g=1
    h=g
    if AT[0]!=0:
        running_queue.append((0,'dash',AT[0]))
        count=AT[0]
    
    ready_queue.append(processes[0])
    
    while not ready_queue[i]=='':
        j=0
        s=ready_queue[i]
        z=processes[j]
        while s!=z:
            j=j+1
            z=processes[j]
        
        if Time_quatum > TBT[j]:
            x=int(TBT[j]+count)
            TBT[j]=0
            running_queue.append((count,processes[j],x))
            count=x
        
        else:
            running_queue.append((count,processes[j],count+Time_quatum))
            TBT[j]-=Time_quatum
            count+=Time_quatum
            
        if g<len(processes):
            k=j+1
            while not k==len(processes):
                if AT[k]<=count and AT[g]==AT[k]:
                    ready_queue.append(processes[k])
                    g=g+1
                k=k+1
        
        if TBT[j]!=0:
            ready_queue.append(processes[j])
        
        if TBT[j]==0 and h==g and g!=len(processes):
            dk=list(AT[x] for x in range(j+1,len(AT)))
            minimum=min(dk)
            print(dk)
            print(minimum)
            running_queue.append((count,'dash',minimum))
            count=minimum
            ready_queue.append('dash')
            i=i+1
            if g<len(processes):
                k=j+1
                while not k==len(processes):
                    if AT[k]<=count and AT[g]==AT[k]:
                        ready_queue.append(processes[k])
                        g=g+1
                    k=k+1
            
            
            
            
        res=all(ele==0 for ele in TBT)
        
        if res:
            ready_queue.append('')
            
        i=i+1
        h=g

        
def display_queues(ready_queue,running_queue):
    print(ready_queue)
    print(running_queue)

def main_calculation(processes,running_queue):
    i=0
    print("P\tAT\tBT\tCT\tTAT\tWT")
    while i<len(processes):
        s=processes[i]
        count=0
        for j in range(len(running_queue)):
            d=list(running_queue[j])
            if d[1]==s:
                count=d[2]
        
        CT.append(count)
        TAT.append(count-AT[i])
        WT.append(TAT[i]-BT[i])
        print(processes[i]+"\t"+str(AT[i])+"\t"+str(BT[i])+"\t"+str(CT[i])+"\t"+str(TAT[i])+"\t"+str(WT[i]))
        i=i+1
    


    
check=''

Time_quatum=0
processes=[]
AT=[]
BT=[]
TBT=[]
CT=[]
TAT=[]
WT=[]
RT=[]

ready_queue=[]
running_queue=[]

# (0,'p2',9) element of running queue


Time_quatum=int(input("Enter value of time quatum:"))

while not check=='end':
    process=input("Enter process name:")
    processes.append(process)
    a=int(input("Enter Arrival time:"))
    AT.append(a)
    b=int(input("Enter Burst time:"))
    BT.append(b)
    TBT.append(b)
    print("Enter any letter to continue or 'end' to end:")
    check=input("=>")
    
print(processes)
print(AT)
print(BT)
round_robin(processes,AT,BT)
display_queues(ready_queue,running_queue)
main_calculation(processes,running_queue)