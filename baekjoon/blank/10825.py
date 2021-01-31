N = int(input())

numList = []
for i in range(N):
    name, x, y, z= input().split()
    numList.append((name,int(x),int(y),int(z)))

numList = sorted(numList, key = lambda x : (-x[1], x[2],-x[3],x[0]))

for i in range(N):
    print(numList[i][0])