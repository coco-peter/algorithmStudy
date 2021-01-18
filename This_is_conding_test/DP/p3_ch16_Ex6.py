
str1 = input()
str2 = input()

def changeAtoB(A,B):
    lenA = len(A)
    lenB = len(B)

    dp = [ [0] * (lenB + 1) for _ in range(lenA + 1)]

    for i in range(1,lenB + 1):
        dp[0][i] = i
    for i in range(1, lenA + 1):
        dp[i][0] = i


    for y in range(1, lenA + 1):
        for x in range(1, lenB + 1):
            if B[x-1] == A[y-1] :
                dp[y][x] = dp[y-1][x-1]
            else:
                dp[y][x] = 1 + min(dp[y-1][x], dp[y][x-1], dp[y-1][x-1])

    return dp[lenA][lenB]

print(changeAtoB(str1,str2))