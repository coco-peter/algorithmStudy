# 8 2 7 3 0 1 9 6 5 4
# 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 0 0


numList = list(map(int, input().split()))

# 선택정렬
# for i in range(0, len(numList)):
#     for j in range(i, len(numList)):
#         if numList[i] > numList[j]:
#             numList[i], numList[j] = numList[j], numList[i]
#
# print(numList)


# 삽입정렬
for i in range(0, len(numList)):
    for j in range(i, -1, -1):
        if numList[i] < numList[j]:
            numList[i], numList[j] = numList[j], numList[i]

print(numList)

# 퀵 정렬


# 퀵 정렬 개선

# 계차수열
