# 7 2
# 1 1 2 2 2 2 3

N, X = map(int, input().split())

numList = list(map(int, input().split()))

start, end = 0, len(numList) -1

def binarySearchFirst(array, start, end, target):

    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == 0 or array[mid -1] < target) and array[mid] == target:
        return mid
    elif array[mid] >= target :
        return binarySearchFirst(array,start,mid -1, target)
    else:
        return binarySearchFirst(array, mid + 1,end, target)


def binarySearchEnd(array, start, end, target):

    if start > end:
        return None

    mid = (start + end) // 2

    if (mid == len(array) -1 or array[mid + 1] > target) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearchEnd(array, start, mid - 1, target)
    else:
        return binarySearchEnd(array, mid + 1, end, target)

def checkCountTarget(numList,start,end,X):

    First = binarySearchFirst(numList,start,end,X)

    if First == None:
        print("hi")
        return -1

    End = binarySearchEnd(numList,start,end,X)

    return End - First + 1

print(checkCountTarget(numList,start,end,X))