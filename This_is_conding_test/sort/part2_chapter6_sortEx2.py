# 2
# 홍길동 95
# 이순신 77

N = int(input())

nameAndScoreList = []

def setting(data):
        return data[1]

for i in range(N):
        (name, score) = input().split()
        nameAndScoreList.append((name,int(score)))

nameAndScoreList = sorted(nameAndScoreList, key = setting)

for student in nameAndScoreList:
        print("%s " %student[0], end="")