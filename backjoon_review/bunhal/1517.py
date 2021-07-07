import sys

input = sys.stdin.readline

N = int(input())

numList = list(map(int, input().split()))
cnt = 0
def merge_sort(list):
    global cnt

    if len(list) <= 1:
        return

    start = 0
    end = len(list)
    mid = (start + end) // 2

    leftList = list[start:mid +1]
    rightList = list[mid+1:]

    temp = []
    left, right = 0, 0
    while left < len(leftList) and right < len(rightList):
        if leftList[left] > rightList[right]:
            temp.append(rightList[right])
            right += 1
            cnt += len(leftList) - left
        else:
            temp.append(leftList[left])
            left += 1

merge_sort(numList)
print(cnt)