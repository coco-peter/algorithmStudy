import sys

input = sys.stdin.readline

N = int(input())
graph = [[" " for _ in range(N)] for _ in range(N)]

def printStar(x, y, size):

    if size == 1:
        graph[y][x] = "*"
        return

    nextSize = size // 3

    for yy in range(3):
        for xx in range(3):
            if yy != 1 or xx != 1:
                printStar(x + xx * nextSize, y + yy * nextSize, nextSize)

    # print(size // 3, size // 3 * 2)
printStar(0,0,N)

for y in range(N):
    for x in range(N):
        print(graph[y][x], end="")
    print("")