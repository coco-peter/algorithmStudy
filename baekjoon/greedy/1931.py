import sys

input = sys.stdin.readline

N = int(input())

timeList = []
for _ in range(N):
    startTime, endTime = map(int,input().split())
    timeList.append((startTime, endTime))

timeList = sorted(timeList, key = lambda x : (x[1], x[0]))

cnt = 1
endTime = timeList[0][1]
for i in range(1,N):
    if timeList[i][0] >= endTime:
        print(timeList[i][0],timeList[i][1])
        endTime = timeList[i][1]
        cnt += 1
# print(timeList)
print(cnt)