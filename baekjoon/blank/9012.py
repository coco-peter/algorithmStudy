import sys

input = sys.stdin.readline

N = int(input())

for i in range(N):
    data = list(input())
    cnt = 0
    isOpened = False
    for j in range(len(data)-1):
        if data[j] == "(":
            cnt += 1
            isOpened = True
        else:
            cnt -= 1
            if cnt == 0:
                isOpened = False
            elif cnt < 0:
                isOpened = True
                break
    if isOpened == False:
        print("YES")
    else:
        print("NO")