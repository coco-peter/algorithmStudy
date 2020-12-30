# 4
# 1 3 1 5

N = int(input())

# 정답
array = list(map(int, input().split()))

d = [0] * 100
d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[N-1])

# 내 방식
# 틀리진 않았을것 같지만, 결국 DP는 한가직 식으로만 구현이 가능해야한다는 점이다...
# 그리고 max는 변수명으로 절대 쓰지 말자 !!!!
riceList = list(map(int, input().split()))
riceList.insert(0,0)

dp = [0] * 101
dp[1] = riceList[1]
dp[2] = riceList[2]

def DP(target):

    if target == 1 or target == 2 or target == 0:
        return dp[target]

    if dp[target] != 0:
        return dp[target]

    dp[target] = max(DP(target -2), DP(target - 3)) + riceList[target]

    return dp[target]

maxValue = 0
for i in range(1,N+1):
    if maxValue < DP(i):
        maxValue = DP(i)

print(maxValue)