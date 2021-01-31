import sys
input = sys.stdin.readline

N = int(input())
numList = []
for i in range(N):
    command = list(input().split())
    if command[0] == "push":
        numList.append(int(command[1]))
    elif command[0] == "pop":
        if len(numList) == 0:
            print("-1")
        else:
            print(numList[len(numList)-1])
            del numList[len(numList)-1]

    elif command[0] == "size":
        print(len(numList))
    elif command[0] == "empty":
        if len(numList) == 0:
            print("1")
        else:
            print("0")
    elif command[0] == "top":
        if len(numList) == 0:
            print("-1")
        else:
            print(numList[len(numList)-1])
