# 4 6
# 19 15 10 17

import sys
N, M = map(int, input().split())
x = list(map(int, sys.stdin.readline().split()))

# 이진탐색으로 훨씬 빠른 속도로 탐색을 할 수 있다.
# 꼭 정렬된 데이터가 아니여도 이진탐색은 시간복잡도를 줄이는 방면에서 사용될수 있으니 참고하자
# 즉 문제를 잘 읽자.
start = 0
end = max(x)
while start <= end:
    mid = (start + end) // 2
    result = 0
    for i in x:
        if i - mid > 0:
            result += i - mid
    if result > M:
        start = mid + 1
    elif result < M:
        end = mid - 1
    else:
        break

print(mid)

# 순차탐색으로 하면 시간 초과를 받을것이다.
# '절단기의 높이'가 최대 10억까지 정수라는 점을 생각해보면 이진 탐색을 생각해보자 이 문제는 파라메트릭 서치라고도 한다.
# cutHeight = 1
# min = 0
# while True:
#     temp = x
#     restlist = []
#     for i in temp:
#         if i < cutHeight:
#             restlist.append(0)
#         else:
#             restlist.append(i-cutHeight)
#
#     if sum(restlist) >= M:
#        if min < cutHeight:
#            min = cutHeight
#     else:
#         break
#     cutHeight += 1




print(min)