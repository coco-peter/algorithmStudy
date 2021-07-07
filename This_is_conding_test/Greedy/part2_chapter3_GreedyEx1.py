# ex1
# 26minutes

N, M, K = map(int, input().split())

numberArr = input().split()


numberArrSorted = sorted(numberArr, reverse=True)

print(numberArrSorted)

checkSameNumber = 0
sumNumber = 0
listIndex = 0
isCheck = 0
for i in range(0,M):
     # print(int(numberArrSorted[listIndex]))
     sumNumber = sumNumber + int(numberArrSorted[listIndex])
     checkSameNumber = checkSameNumber + 1
     if isCheck == 1:
         listIndex = listIndex - 1
         checkSameNumber = 1
         isCheck = 0
     else :
         if checkSameNumber == K:
             checkSameNumber = 1
             listIndex = listIndex + 1
             isCheck = 1

     # print("sum %d" %sumNumber)
     # print(checkSameNumber)


print(sumNumber)
