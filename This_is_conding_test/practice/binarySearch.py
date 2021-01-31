# 5
# 8 3 7 9 2
# 3
# 5 7 9


N = int(input())
numList = list(map(int, input().split()))
numList = sorted(numList)

def binarySearch(array, start, end, target):

    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return array[mid]
    elif array[mid] < target:
        return binarySearch(array, mid + 1, end, target)
    else:
        return binarySearch(array, start, mid -1, target)

M = int(input())
findList = list(map(int,input().split()))
isStock = None
for i in findList:
    isStock = binarySearch(numList,0,len(numList),i)
    if isStock == None:
        print("없어")
    else:
        print("있어")
