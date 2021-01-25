N = int(input())

for i in range(1, N+1):
    if i == N:
        for j in range(2*i -1):
            print("*", end="")
    else:
        for j in range(N-i):
            print(" ", end="")
        print("*", end="")
        for j in range(2*(i-1) -1):
            print(" ", end="")
        if i != 1:
            print("*", end="")

    print("")
