# 5
# 8 3 7 9 2
# 3
# 5 7 9



N = int(input())
productList = list(map(int, input().split()))

M = int(input())
requestList = list(map(int, input().split()))

# binary search def
def binarySearch(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        end = mid - 1
        return binarySearch(array, target, start, end)
    else:
        start = mid + 1
        return binarySearch(array, target, start, end)


productList = sorted(productList)
for i in range(M):
    isStock = binarySearch(productList,requestList[i],0,N-1)
    if isStock != None:
        print("yes")
    else:
        print("no")
