

N = int(input())

res = 1
for i in range(2,N+1):
    res *= i

strRes = str(res)

cnt = 0
for i in strRes[::-1]:
    if i == "0":
        cnt += 1
    else:
        break
print(cnt)
