
# 푸는 방법은 떠올랐는데
# 구현 방법이 너무 더러웠다...
# 아래 예시는 정답지...
# 아직 멀었다...

X = int(input())

data = [0] * 30001



for i in range(2, X + 1):
    data[i] = data[i-1] + 1

    if i % 2 == 0:
        data[i] = min(data[i], data[i // 2] + 1)
    if i % 3 == 0:
        data[i] = min(data[i], data[i // 3] + 1)
    if i % 5 == 0:
        data[i] = min(data[i], data[i // 5] + 1)

print(data[X])

