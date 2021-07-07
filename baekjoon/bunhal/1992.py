import sys

input = sys.stdin.readline

N = int(input())

mapData = [[0] * N for _ in range(N)]

for y in range(N):
    numList = list(map(int,input().strip()))
    for x in range(N):
        mapData[y][x] = numList[x]

def cutData(x, y, size):
    num = mapData[y][x]

    if size == 1:
        print(num, end="")
        return

    isSameAll = True
    for yy in range(y,y+size):
        for xx in range(x, x+size):
            if num != mapData[yy][xx]:
                isSameAll = False
                break

    if not isSameAll:
        print("(", end="")
        for yy in range(y, y + size , size // 2):
            for xx in range(x, x + size, size // 2):

                cutData(xx, yy, size // 2)
        print(")", end="")
    else:
        print(num,end="")

cutData(0,0,N)