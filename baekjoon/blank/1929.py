

N, M = map(int,input().split())
a = [False,False] + [True]*(M-1)

# 에라토스테네스의 체 -- > 소수 판별
# 2의 배수를 싹다 False 처리
# 그다음 True중 가장 작은거의 배수 싹다 False
# 반복



for i in range(2,M+1):
  if a[i]:
    if i >= N:
        print(i)
    for j in range(2*i, M+1, i):
        a[j] = False
