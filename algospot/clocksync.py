import sys

input = sys.stdin.readline



max_switch = 10
INF = max_switch * 3 + 1

switchTable = [
    [0, 1, 2],
    [3, 7, 9, 11],
    [4, 10, 14, 15],
    [0, 4, 5, 6, 7],
    [6, 7, 8, 10, 12],
    [0, 2, 14, 15],
    [3, 14, 15],
    [4, 5, 7, 14, 15],
    [1, 2, 3, 4, 5],
    [3, 4, 5, 9, 13]
]



def moveTime(clocks, cnt):

    for i in switchTable[cnt]:
        clocks[i] += 3
        if clocks[i] == 15:
            clocks[i] = 3


def isAllSetHour(clocks):
    for i in clocks:
        if i != 12:
            return False

    return True

def setTime(clocks, cnt):

    if cnt ==  max_switch:
        if isAllSetHour(clocks):
            return 0
        else:
            return INF

    res = INF

    for i in range(0,4):
        temp = i + setTime(clocks, cnt + 1)
        res = min(res, temp)
        moveTime(clocks, cnt)

    return res


if __name__ == "__main__":

    for C in range(int(input())):
        clocks = list(map(int,input().split()))

        res = setTime(clocks, 0)

        if res == INF:
            print(-1)
        else:
            print(res)

