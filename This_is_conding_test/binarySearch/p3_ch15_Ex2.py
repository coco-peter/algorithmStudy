
# 5
# -15 -6 1 3 7

# 7
# -15 -4 2 8 9 13 15

# 7
# -15 -4 3 8 9 13 15

N = int(input())

numList = list(map(int, input().split()))

def binarySearch(numList, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if mid == numList[mid]:
        return numList[mid]
    elif mid > numList[mid]:
        # 재귀로 들어갈때는 항상 return으로 들어가야 none이 반환이 안된다 !!!!!
        return binarySearch(numList, mid + 1, end)
    else:
        return binarySearch(numList,start, mid-1)


result = binarySearch(numList,0,N-1)
if result == None:
    print(-1)
else:
    print(result)

