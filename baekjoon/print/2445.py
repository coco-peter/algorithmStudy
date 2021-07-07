N = int(input())

for i in range(1,N+1):
    for j in range(i):
        print("*", end="")
    for k in range((N-i) * 2):
        print(" ", end="")
    for h in range(i):
        print("*", end="")

    print("")

for i in range(1,N+1):
    for j in range(N-i):
        print("*", end="")
    for k in range(i * 2):
        print(" ", end="")
    for h in range(N-i):
        print("*", end="")

    print("")