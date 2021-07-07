# 5
# 3 2 1 1 9

# about 1h
# 많은 테스트 케이스를 못 보는게 좀 아쉽다.
# 일단 답지랑 비교해보자.

N = int(input())
a = list(map(int, input().split()))

minNum = 1
isfindMinNum = 1
sum = 0

while isfindMinNum == 1:
    isfindMinNum = 0
    # print("현재 min값 : %d" %minNum)


    for i in range(0,len(a)):
        sum += a[i]
        if minNum == sum:
            isfindMinNum = 1
            # print("find 1: %d" % minNum)
            break
        isfindMinNum != 1
        for j in range(i+1,len(a)):
                sum += a[j]
                if minNum == sum:
                    isfindMinNum = 1
                    # print("find 2: %d" %minNum)
                    # print(sum)
                    # break
                # else:
                    # print(sum)

        sum = 0




    if isfindMinNum == 0:
        print("최소값은 : %d" % minNum)
        break
    else:
        minNum += 1

