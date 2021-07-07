N = int(input())

numList = []
index = 0
for i in range(N):
    x, y = input().split()
    numList.append((int(x),y,index))
    index += 1

numList = sorted(numList, key = lambda x : (x[0], x[2]))

for i in range(N):
    print(numList[i][0], numList[i][1])