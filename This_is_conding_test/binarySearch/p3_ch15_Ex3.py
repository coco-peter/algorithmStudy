# https://www.acmicpc.net/problem/2110

from itertools import combinations


N, C = list(map(int, input().split(' ')))

numList = []

for _ in range(N):
    numList.append(int(input()))

numList.sort()

# start = numList[1] - numList[0] # 최소 gap
start = 1 # 최소 gap
end = numList[-1] - numList[0]  # 최대 gap

result = 0
while(start <= end):
    mid = (start + end) // 2            # 특정 gap에 대해 모든 집 거리 비교
    value = numList[0]
    count = 1

    for i in range(1,N):
        # ex) 2번째 집과 1번째 집거리가 value + mid보다 크다면 gap을 만족한다는 것 == 공유기 설치
        # 안크면 공유기 설치 안하고 넘어가는거임
        if numList[i] >= value + mid:
            value = numList[i]
            count += 1

    # count가 C를 만족해도 더 큰 경우가 나올 수 있으므로 계속 해보는거다.
    # 물론 count가 C보다 크면 안되니까 start = mid + 1 하는것이고
    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1

print(result)

# candidates = combinations(numList, C)
# maxValue = 0
# for candidate in candidates:
#
#
#     a, b, c = candidate[0], candidate[1], candidate[2]
#     if abs(a-b) == 1 or abs(b-c) == 1:
#         continue
#
#     if abs(a-b) < abs(b-c):
#         if maxValue < abs(a-b):
#             maxValue = abs(a-b)
#     else:
#         if maxValue < abs(b-c):
#             maxValue = abs(b-c)
#

