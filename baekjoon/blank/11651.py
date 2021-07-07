N = int(input())

numList = []
for i in range(N):
    x, y = map(int,input().split())
    numList.append((x,y))

numList = sorted(numList, key = lambda x : (x[1], x[0]))

for i in range(N):
    print(numList[i][0], numList[i][1])