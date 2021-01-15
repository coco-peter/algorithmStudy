# https://programmers.co.kr/learn/courses/30/lessons/42889

N = 5

stages = [2, 1, 2, 6, 2, 4, 3, 3]

def solution(N, stages):
    rateFail = 0
    rateFailNstage = []
    passedCount = len(stages)

    for i in range(1,N+1):
        passedButNotClearCount = stages.count(i)

        if passedButNotClearCount == 0:
            rateFail = 0
        else:
            rateFail = passedButNotClearCount / passedCount

        passedCount -= passedButNotClearCount
        rateFailNstage.append((rateFail, i))

    rateFailNstage = sorted(rateFailNstage, key = lambda x : (-x[0], x[1]))

    sortedStage = []
    for i in range(len(rateFailNstage)):
        sortedStage.append(rateFailNstage[i][1])


    return sortedStage

print(solution(N,stages))