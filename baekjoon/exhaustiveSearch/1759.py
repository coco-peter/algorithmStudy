import sys
from itertools import combinations

input = sys.stdin.readline

L , C = map(int,input().split())

wordList = list(map(str,input().split()))

candidates = combinations(wordList, L)

m_word = ["a", "e", "i", "o", "u"]

res = []
for candidate in candidates:
    candidate = sorted(candidate)
    m_wordCnt = 0
    j_wordCnt = 0
    # print(candidate)
    for i in range(L):
        if candidate[i] in m_word:
            m_wordCnt += 1
        else:
            j_wordCnt += 1

    if m_wordCnt >= 1 and j_wordCnt >= 2:
        res.append("".join(candidate))

res = sorted(res)
for i in res:
    print(i)
