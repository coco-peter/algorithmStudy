import sys
input=sys.stdin.readline

def merge(a,b):
    global cnt
    la,lb=len(a),len(b)
    i,j=0,0
    temp=[]
    while i<la and j<lb:

    return temp

def merge_sort(arr):
    if len(arr)<=1:
        return arr
    left=0
    right=len(arr)-1
    mid=(left+right)//2
    return merge(merge_sort(arr[left:mid+1]),merge_sort(arr[mid+1:]))

n=int(input())
max = 0
arr = []
for i in range(n):
    x,y =map(int,input().split())
    arr.append((x,y))
merge_sort(arr)
print(cnt)