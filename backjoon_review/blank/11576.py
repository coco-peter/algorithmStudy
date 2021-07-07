import sys


input = sys.stdin.readline

A, B = map(int,input().split())

m = int(input())

numList = list(map(int,input().split()))

# binaryList = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
#               "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]
binaryList = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19 , 20 , 21, 22 , 23,
                24, 25, 26, 27, 28, 29]


def changeBtoN(B, N, res):
    index = 0
    for i in range(m):
        # print(B, N, B[i], binaryList[B[i]], pow(N, index), res)
        res += B[-1] * (N ** index)
        index += 1
        B.pop(-1)
    return res


def changeNtoB(N, B, res):
    # print(N, B, res)
    if N < B:
        res.append(str(binaryList[N]))
        return res[::-1]

    res.append( str(binaryList[N % B]) )
    N = N // B

    return changeNtoB(N, B, res)

resultBtoN = changeBtoN(numList, A , 0)
resultNtoB = changeNtoB(resultBtoN, B, [])

print(" ".join(resultNtoB))

