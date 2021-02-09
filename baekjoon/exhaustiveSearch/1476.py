import sys

input = sys.stdin.readline


E, S , M = map(int,input().split())

E2 = S2 = M2 = 1
years = 1
while True:
    if E2 == E and S == S2 and M == M2:
        break

    if E2 < 15:
        E2 += 1
    else:
        E2 = 1

    if S2 < 28:
        S2 += 1
    else:
        S2 = 1

    if M2 < 19:
        M2 += 1
    else:
        M2 = 1

    years += 1

print(years)