N = input()
N = sorted(N, reverse = True)

sum = 0
if "0" not in N:
    print("-1")
else:
    for i in N:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print("".join(N))