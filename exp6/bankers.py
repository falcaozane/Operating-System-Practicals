n = 5
m = 3
alloc = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]
max = [[8, 5, 3], [3, 2, 2], [12, 0, 2], [2, 4, 2], [4, 9, 3]]
avail = [3, 3, 2]
f = [0] * n
ans = [0] * n
ind = 0
need = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        need[i][j] = max[i][j] - alloc[i][j]
y = 0
for k in range(5):
    for i in range(n):
        if f[i] == 0:
            flag = 0
            for j in range(m):
                if need[i][j] > avail[j]:
                    flag = 1
                    break
            if flag == 0:
                ans[ind] = i
                ind += 1
                for y in range(m):
                    avail[y] += alloc[i][y]
                f[i] = 1               
flag = 1
for i in range(n):
    if f[i] == 0:
        flag = 0
        print("The following system is not safe")
        break
if flag == 1:
    print("Following is the SAFE Sequence")
    for i in range(n - 1):
        print("P",ans[i],end='->')
    print("P",ans[n - 1])




