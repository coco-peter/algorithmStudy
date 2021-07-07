# 10 minutes

N = input()
A = list(N)

frontSum = 0
endSum = 0
for i in range(0,len(A)):
    if i < len(A) / 2:
        frontSum += int(A[i])
    else:
        endSum += int(A[i])

if frontSum == endSum:
    print("LUCKY")
else:
    print("READY")