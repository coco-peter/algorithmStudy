


A, P = map(int,input().split())

numList = []
isVisited = []
numList.append(A)
nextA = 0

while True:
    strA = str(A)
    endPoint = -1
    nextA = 0
    for i in range(len(strA)):
        nextA += int(strA[i]) ** P
    for i in range(len(numList)):
        if nextA == numList[i]:
            endPoint = i
            break
    if endPoint > -1:
        break
    else:
        numList.append(nextA)
    A = nextA
print(len(numList[:endPoint]))

print( 9 ** 5)