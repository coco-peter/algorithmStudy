

daysPerMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
month, day = map(int,input().split())

alldays = 0
for i in range(0, month):
    alldays += daysPerMonth[i]
alldays += day

print(days[alldays % 7])
