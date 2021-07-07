# https://programmers.co.kr/learn/courses/30/lessons/60062

# 12
# 1 5 6 10
# 1 2 3 4

from itertools import permutations


n = int(input())

weak = list(map(int, input().split()))

dist = list(map(int, input().split()))


def solution(n,weak,dist):

    # 시계방향과 반시계 방향구현을 위해 weak를 연장
    weak_length = len(weak)
    for i in range(weak_length):
        weak.append(weak[i] + n)

    # print(weak)

    answer = len(dist) + 1

    # 0 ~ weak_length 까지만 반복해보면 됨.
    for i in range(weak_length):

        # i를 기준으로 weak_length 만큼 담는다.
        startPosition = [weak[i] for i in range(i,i+weak_length)]

        # 후보자들을 순열로 조합의 경우를 나눈다.
        candidates = permutations(dist,len(dist))

        # 조합들을 하나씩 돌려본다.
        for candidate in candidates:

            idx, count = 0, 1

            # 조합들 중 첫번째 사람이 할수 있는시간을 startPostion[idx]를 더해주면 최대 가능한 거리가 나온다.
            maxLength = candidate[0] + startPosition[idx]

            # weak_length 길이만큼 반복을 한다.
            for j in range(weak_length):

                # 만약 최대길이가 startPostion[j]보다 작다면 거기가 최대치라는 뜻이므로
                if maxLength < startPosition[j]:

                    # 사람을 추가한다.
                    count += 1

                    # 만약 사람이 후보자들 숫자보다 많다면 그만해야한다.
                    if count > len(candidate):
                        break

                    # 그리고 idx를 하나 추가시켜주는데
                    idx += 1

                    # 이는 다음 사람이 할 수 있는 최대 거리를 갱신하기 위해서이다.
                    maxLength = candidate[idx] + startPosition[j]

            # 바로 위 반복문을 돌고 나면 첫 후보 조합에 대한 결과가 나올것이다.
            # 만약 if maxLength < startPosition[j]: 에 계속 해당되지 않으면 1로 나올것이다.
            answer = min(answer, count)

    if answer > len(dist):
        return -1

    return answer




solution(n,weak,dist)