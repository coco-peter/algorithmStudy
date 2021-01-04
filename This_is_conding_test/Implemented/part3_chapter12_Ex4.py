
# 와...
# 내가 구현한건 rotation정도...
# 근데 기존에 내가 짠 코드에서 어떤 부분이 걸린걸까??
# Test case 3개정도를 못통과했는데 ㅠㅠ

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotationKey(key):
    rotatedKey = [[0] * len(key[0]) for i in range(len(key))]

    for x in range(len(key)):
        for y in range(len(key[0])):
            rotatedKey[x][len(key[0]) - 1 - y] = key[y][x]

    return rotatedKey

def checkMatch(newLock):
    for y in range(len(newLock) // 3, len(newLock) // 3 * 2):
        for x in range(len(newLock) // 3, len(newLock) // 3* 2):
            if newLock[y][x] != 1:
                return False

    return True


def solution(key, lock):
    keyWidth = len(key)
    keyHeight = len(key[0])
    lockWidth = len(lock)
    lockHeight = len(lock[0])
    emptySpace = 0

    checkMap = [[0] * (lockHeight * 3) for i in range(lockHeight * 3)]

    for y in range(lockHeight):
        for x in range(lockWidth):
            checkMap[y + lockHeight][x + lockWidth] = lock[y][x]

    print(checkMap)
    for y in range(lockHeight * 2):
        for x in range(lockWidth * 2):
            rotatedKey = key
            for rotation in range(4):
                rotatedKey = rotationKey(rotatedKey)
                for i in range(len(rotatedKey)):
                    for j in range(len(rotatedKey)):
                        checkMap[y+i][x+j] += rotatedKey[i][j]

                if checkMatch(checkMap):
                    # print(rotatedKey)
                    return True

                for i in range(len(rotatedKey)):
                    for j in range(len(rotatedKey)):
                        checkMap[y+i][x+j] -= rotatedKey[i][j]


    return False


print(solution(key,lock))

