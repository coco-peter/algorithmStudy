import sys

input = sys.stdin.readline

N = int(input())

costList = list(map(int,input().split()))

costList = sorted(costList)
costPerPeople = []

cost = 0

for i in range(N):
    cost += costList[i]
    costPerPeople.append(cost)

print(sum(costPerPeople))

