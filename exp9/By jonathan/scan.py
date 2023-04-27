reqSequence = [82,170,43,140,24,16,190]
initialHead = 50
diskrange = 199

left = [x for x in reqSequence if x<=50]
left.sort(reverse=True)
left.append(0)
right = [x for x in reqSequence if x>50]
right.sort()

# print(left)
# print(right)
current = initialHead
order = []
totalSeek = 0

for i in range(len(left)):
    towards = left[i]
    order.append(left[i])
    totalSeek = totalSeek + abs(towards-current)
    current = towards
    
for i in range(len(right)):
    towards = right[i]
    order.append(right[i])
    totalSeek = totalSeek + abs(towards-current)
    current = towards
    
print(f"Order of execution: {order}")
print(f"Total Seek: {totalSeek}")
    