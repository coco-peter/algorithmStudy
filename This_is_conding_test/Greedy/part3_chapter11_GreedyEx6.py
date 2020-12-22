# 뭔가 로직은 맞다고 생각했는데, 테스트를 모두 통과 하지 못했다.
# 답을 보고 왜 그렇게 했는지 생각해보자


timePerFood = list(map(int, input().split()))
k = int(input())

def solution(food_times, k):
    answer = 0
    for i in range(0,k+1):
        if food_times[answer] > 0 :
            food_times[answer] -= 1
            # print("#A %d ~ %d 초 동안 %d번 음식을 섭취한다 . 남은시간은 " % (i, i + 1, answer + 1) + str(food_times) + " 입니다 ")

            if i == k:
                return answer + 1

            if sum(food_times) == 0:
                answer = -1
                return answer

            answer += 1
            if answer == len(food_times):
                answer = 0
        else:
            while True:
                answer += 1
                if answer == len(food_times):
                    answer = 0
                if food_times[answer] > 0:
                    food_times[answer] -= 1
                    # print("#B %d ~ %d 초 동안 %d번 음식을 섭취한다 . 남은시간은 " % (i, i + 1, answer + 1) + str(food_times) + " 입니다 ")
                    # print("총합 : %d" % sum(food_times))

                    if i == k:
                        return answer + 1

                    if sum(food_times) == 0:
                        answer = -1
                        return answer
                    break

    # return answer

result= solution(timePerFood,k)
# print(result)