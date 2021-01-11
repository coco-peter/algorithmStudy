# https://programmers.co.kr/learn/courses/30/lessons/60058

p = input()

def checkBalance(w):
    count = 0

    for i in range(len(w)):
        if w[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            return i


def checkRight(w):
    pair = 0

    for i in range(len(w)):

        if w[i] == "(":
            pair += 1
        else:
            if pair == 0:
                return False
            pair -= 1


    return True



def solution(p):


    answer = ''

    # 빈 배열이면 return
    if p == '':
        return answer

    index = checkBalance(p)
    u = p[:index+1]
    v = p[index+1:]
    if checkRight(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        u = list(u[1:-1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        answer += "".join(u)
    return answer
answer = solution(p)


print(answer)