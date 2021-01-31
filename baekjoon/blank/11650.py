N = int(input())

numList = []
for i in range(N):
    x, y = map(int,input().split())
    numList.append((x,y))

numList = sorted(numList, key = lambda x : (x[0], x[1]))

for i in range(N):
    print(numList[i][0], numList[i][1])