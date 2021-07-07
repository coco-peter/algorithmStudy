

n = int(input())

Dp = [1] * 1001
Dp[1] = 1

num = 2
count = 1

def checkPrime(num):

    if num % 2 == 0:
        if Dp[num // 2] != 0:
            Dp[num] = 1
            return True
    elif num % 3 == 0:
        if Dp[num // 3] != 0:
            Dp[num] = 1
            return True
    elif num % 5 == 0:
        if Dp[num // 5] != 0:
            Dp[num] = 1
            return True

    return False



while count < n:
    result = checkPrime(num)
    if result:
        # print(num)
        count += 1
    num += 1

print(num-1)



