
#13m
#런타임 에러는 배열 인덱스 참조 오류일수 있으니 참고 !

N = int(input())

dp = [ [0] * (10) for _ in range(1001)]

for i in range(10):
    dp[1][i] = 1

for y in range(2,N+1):
    for x in range(10):
        dp[y][x] = sum(dp[y-1][x:])

print(sum(dp[N][:]) % 10007)
