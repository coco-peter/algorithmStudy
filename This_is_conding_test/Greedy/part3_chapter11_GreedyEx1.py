# 5
# 2 3 1 2 2
# 26 minutes

N = int(input())
a = list(map(int, input().split()))

a = sorted(a)

numberGroup = 0
numberPerson = 0
min = 0

for i in a:
    min = i
    numberPerson += 1
    if min == numberPerson:
        numberPerson = 0
        min = 0
        numberGroup += 1

print(numberGroup)