#20m

array = list(input())

stick = 0
cuttedCnt = 0
laizer = 0


for i in range(len(array)-1):
    if array[i] == "(" and array[i+1] == ")":
        if stick == 0:
            continue
        else:
            cuttedCnt += stick
    elif array[i] == "(" and array[i+1] == "(":
        stick += 1
        cuttedCnt += 1
    elif array[i] == ")" and array[i+1] == ")":
        stick -= 1


print(cuttedCnt)
