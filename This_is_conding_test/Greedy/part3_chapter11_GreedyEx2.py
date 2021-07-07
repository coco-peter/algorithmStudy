# 12 minutes

num = list(input())

result = 0
for i in num:
    i = int(i)
    if i == 0 or i == 1:
        result += i
    else:
        if result == 0:
            result += i
        else:
            result *= i


print(result)