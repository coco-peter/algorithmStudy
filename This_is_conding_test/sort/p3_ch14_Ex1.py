# https://www.acmicpc.net/problem/10825

# time : 13m

N = int(input())

scoreNname = []

for i in range(N):
    Name, korean, english, math = input().split()
    scoreNname.append((Name, int(korean), int(english), int(math)))

scoreNname = sorted(scoreNname, key = lambda x : (-x[1], x[2], -x[3], x[0] ))

for name in scoreNname:
    print(name[0])