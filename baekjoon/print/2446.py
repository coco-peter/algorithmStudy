N = int(input())

for i in range(1,N+1):
    for k in range(i-1):
        print(" ", end="")
    for j in range(2*(N-i+1) -1):
        print("*", end="")

    print("")

for i in range(1,N):
    for k in range(N-i-1):
        print(" ", end="")
    for j in range(2*(i+1) -1):
        print("*", end="")

    print("")