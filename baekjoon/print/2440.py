N = int(input())

for i in range(1,N+1):
    for j in range(N-i+1,0,-1):
        print("*", end="")
    print("")