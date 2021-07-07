# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2



T = int(input())

for _ in range(T):

    n, m = map(int,input().split())
    numList = list(map(int, input().split()))

    dp = []
    index = 0
    for i in range(n):
        dp.append(numList[index : index +m])            # tip 하나의 행으로 받아주고 그다음은 자동으로 개행된다. 흠..
        index += m

    for x in range(1,m):
        for y in range(n):
            # 왼쪽 위에서 오는 경우
            if y == 0:
                left_up = 0
            else:
                left_up = dp[y-1][x-1]

            # 왼족 아래에서 오는 경우
            if y == n-1:
                left_bot = 0
            else:
                left_bot = dp[y+1][x-1]

            # 왼쪽에서 오는 경우
            left = dp[y][x-1]

            dp[y][x] = dp[y][x] + max(left, left_up, left_bot)

    result = 0
    for y in range(n):
        result = max(result, dp[y][m-1])

    print(result)
