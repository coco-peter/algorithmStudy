import sys

input = sys.stdin.readline

N = int(input())

mapData = [[0] * N for _ in range(N)]
reslist = [0] * 3
for y in range(N):
    numList = list(map(int,input().split()))
    for x in range(N):
        mapData[y][x] = numList[x]

# print(mapData)

def cutPaper(array, x, y, size):

    num = array[y][x]
    isAllSame = True

    if size == 1:
        reslist[num + 1] += 1
        return

    for yy in range(y, y + size):
        for xx in range(x, x + size):
            if num != array[yy][xx]:
                isAllSame = False
                break
    if not isAllSame:
        for yy in range(y, y + size, size // 3):
            for xx in range(x, x + size, size // 3):
                cutPaper(array, xx, yy, size // 3)
    else:
        reslist[num + 1] += 1
cutPaper(mapData,0,0,N)

for i in reslist:
    print(i)