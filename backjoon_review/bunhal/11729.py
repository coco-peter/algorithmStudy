import sys

input = sys.stdin.readline

N = int(input())
result = 0
process = []
def hanoi(first, second, end, cnt):
    global result
    if cnt == 0:
        return
    hanoi(first, end, second, cnt -1)
    process.append((first, end))
    result += 1
    hanoi(second, first, end, cnt -1)

hanoi(1, 2, 3, N)

print(result)
for i in range(len(process)):
    print(process[i][0], process[i][1])
