# 8 2 7 3 0 1 9 6 5 4
# 9 9 8 8 7 7 6 6 5 5 4 4 3 3 2 2 1 1 0 0

numberList = list(map(int, input().split()))
#

# selectsorted
# for i in range(len(numberList)):
#     for j in range(i+1,len(numberList)):
#         if numberList[i] > numberList[j]:
#             numberList[i], numberList[j] = numberList[j], numberList[i]
# print(selectsorted)

# insert Sort
# for i in range(1,len(numberList)):
#     for j in range(i,0,-1):
#         if numberList[j] < numberList[j-1]:
#             numberList[j], numberList[j-1] = numberList[j-1], numberList[j]
#             print(numberList)
#         else:
#             break

# quick sort
def quick_Sort_org(array, start, end):

    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= len(array) - 1 and array[left] < array[pivot]:
            left += 1
        while right > 0 and array[right] > array[pivot]:
            right -= 1

        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        else:
            array[left], array[right] = array[right], array[left]

    quick_Sort_org(array, start, right - 1)
    quick_Sort_org(array, right + 1, end)

quick_Sort_org(numberList,0, len(numberList) - 1)
print(numberList)

# quick sort_simple
# def quick_Sort(array):
#
#     if len(array) <= 1:
#         return array
#
#     pivot = array[0]
#     tail = array[1:]
#
#     left = [x for x in tail if x <= pivot]
#     right = [x for x in tail if x > pivot]
#
#     return quick_Sort(left) + [pivot] + quick_Sort(right)
#
# quick_Sort(numberList)
# print(quick_Sort(numberList))
#
# quick_Sort_org(numberList, 0 , len(numberList) - 1)
# print(numberList)


# 계수 정렬

checkNum = [0] * (max(numberList) + 1)
for i in numberList:
    checkNum[i] += 1

for i in range(len(checkNum)):
    for j in range(checkNum[i]):
        print("%d " %i, end="")



