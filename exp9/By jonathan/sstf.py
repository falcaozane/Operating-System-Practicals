reqSequence = [45, 21, 67, 90, 4, 89, 52, 61, 87, 25]
initialHead = 50
current = initialHead
m = len(reqSequence)
order = []
totalSeek = 0

while(len(order) != m ):
    n = len(reqSequence)
    seekFromCurrent = [abs(reqSequence[i]-current) for i in range(n)]
    minIndex = seekFromCurrent.index(min(seekFromCurrent))
    totalSeek = totalSeek + min(seekFromCurrent)
    order.append(reqSequence[minIndex])
    current = reqSequence[minIndex]
    reqSequence.remove(reqSequence[minIndex])
    
print(f'Order of execution: {order}')
print(f"Total Seek: {totalSeek}")

