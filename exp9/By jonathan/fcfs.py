# reqSequence = [176, 79, 34, 60, 92, 11, 41, 114]
reqSequence = [45, 21, 67, 90, 4, 50, 89, 52, 61, 87, 25]
InitialHead = 50
current = InitialHead

totalSeek = 0

for i in range(len(reqSequence)):
    towards = reqSequence[i]
    totalSeek = totalSeek + abs(towards-current)
    print(totalSeek)
    current = towards
    
print(f"Total Seek: {totalSeek}")
# in fcfs, the order will be same as request sequence. 
print(f"Order: {reqSequence}")