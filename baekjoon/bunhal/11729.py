import sys

input = sys.stdin.readline

N = int(input())

moveList = []
def hanoi(num,a,b,c):
    if num == 1:
        moveList.append([a,c])
    else:
        hanoi(num-1,a,c,b)
        moveList.append([a,c])
        hanoi(num-1,b,a,c)

hanoi(N,1,2,3)
print(len(moveList))
for i in moveList:
    print(i[0],i[1])
