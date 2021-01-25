# 8 2 7 3 0 1 9 6 5 4
# 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 0 0


numList = list(map(int, input().split()))

# 선택정렬

# for i in range(len(numList)):
#     for j in range(i+1, len(numList)):
#         if numList[i] > numList[j]:
#             numList[i], numList[j] = numList[j], numList[i]
#
# print(numList)

# 삽입정렬
# for i in range(1, len(numList)):
#     for j in range(i,0,-1):
#         if numList[j] < numList[j-1]:
#             numList[j], numList[j-1] = numList[j-1], numList[j]
#
# print(numList)

# 퀵 정렬
#
# def quickSort(array, start, end):
#     if start >= end:
#         return
#
#     pivot = start
#     left = start + 1
#     right = end
#
#     while left <= right:
#         while left <= len(array) -1 and array[left] < array[pivot]:
#             left += 1
#         while right > 0 and array[right] > array[pivot]:
#             right -= 1
#
#         if left > right:
#             array[pivot], array[right] = array[right], array[pivot]
#         else:
#             array[left], array[right] = array[right], array[left]
#
#     quickSort(array,start, right-1)
#     quickSort(array, right+1, end)
#
# quickSort(numList,0, len(numList)-1)
# print(numList)

def quickSort2(array):
    if len(array) <= 1:
       return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x < pivot]
    right = [x for x in tail if x > pivot]

    return quickSort2(left) + [pivot] + quickSort2(right)

sortedList = quickSort2(numList)
print(sortedList)


# 계차수열
# maxValue = max(numList)
# sortedList = [0] * (maxValue+1)
# for k in numList:
#     sortedList[k] += 1
# for i in range(maxValue):
#     while sortedList[i] > 0:
#         print("%d " %i , end=" ")
#         sortedList[i] -= 1

