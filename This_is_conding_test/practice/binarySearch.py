
# 5
# 8 3 7 9 2
# 3
# 5 7 9



N = int(input())
productList = list(map(int, input().split()))

M = int(input())
requestList = list(map(int, input().split()))


def binarySearch(array, target, start, end):

    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array,target,start,mid-1)
    else:
        return binarySearch(array,target,mid+1,end)

for k in requestList:
    isThereTarget = binarySearch(productList,k,0,len(productList)-1)
    if isThereTarget == None:
        print("NO")
    else:
        print("Yes")


