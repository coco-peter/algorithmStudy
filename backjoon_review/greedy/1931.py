import sys

input = sys.stdin.readline

timetable = []
for _ in range(int(input())):
    startTime, endTime = map(int,input().split())
    timetable.append((startTime, endTime))

timetable = sorted(timetable, key = lambda x : (x[1], x[0]))

lastEnd = 0
cnt = 0
for start, end in timetable:
    if lastEnd <= start:
        lastEnd = end
        cnt += 1
        print(start, end)

print(cnt)


