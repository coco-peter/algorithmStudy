# ex2
# 17 minutes


N,M = map(int, input().split())
d = [[0 for i in range(M)] for j in range(N)]
#
# 3 3
# 3 1 2
# 4 1 4
# 2 2 2

# 2 4
# 7 3 1 8
# 3 3 3 4

minNum = 10001
MaxNum = 0
#1
# for y in range(0,N):
#         num = list(map(int,input().split()))
#         for x in range(0,M):
#             d[y][x] = num[x]
#             # print(d[y][x], end="")
#         # print("")
#
#
# # 이 방법이 틀린것은 아니다 다만, 위에서 데이터를 입력 받을때 충분히 시간복잡도를 줄일 수 있는 방법이 있었을 것이다.
# # 즉 구현에만 집중하지 말고 시간복잡도 또한 최소한으로 할 수 있는 방법을 구현하자 !!

# for y in range(0,N):
#         for x in range(0,M):
#             if minNum > d[y][x]:
#                 minNum = d[y][x]
#
#         if MaxNum < minNum:
#             MaxNum = minNum
#         minNum = 10001

#2
# for y in range(0,N):
#         num = list(map(int,input().split()))
#         for x in range(0,M):
#             if minNum > num[x]:
#                 minNum = num[x]
#
#         if MaxNum < minNum:
#             MaxNum = minNum
#         minNum = 10001

#3
# min, max 함수를 써보자
for y in range(0,N):
        num = list(map(int,input().split()))
        minNum = min(num)
        MaxNum = max(MaxNum,minNum)


print(MaxNum)