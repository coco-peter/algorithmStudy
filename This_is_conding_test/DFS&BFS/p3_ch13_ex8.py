# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque

def checkValuablePos(pos, newBorad):
    valuablePos = []
    pos = list(pos)
    curY1, curX1, curY2, curX2 = pos[0][0], pos[0][1], pos[1][0], pos[1][1]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for i in range(4):
        newY1, newX1, newY2, newX2 = curY1 + dy[i], curX1 + dx[i], curY2 + dy[i], curX2 + dx[i]
        if newBorad[newY1][newX1] == 0 and newBorad[newY2][newX2] == 0:
            valuablePos.append({(newY2, newX2), (newY1, newX1)})

    # 가로인 상태
    if curY1 == curY2:
        UP, DOWN = -1, 1
        for i in [UP, DOWN]:
            if newBorad[curY1 + i][curX1] == 0 and newBorad[curY2 + i][curX2] == 0:
                valuablePos.append({(curY1, curX1), (curY1 + i, curX1)})
                valuablePos.append({(curY2, curX2), (curY2 + i, curX2)})
    else:  # 세로인 상태
        LEFT, RIGHT = -1, 1
        for i in [LEFT, RIGHT]:
            if newBorad[curY1][curX1 + i] == 0 and newBorad[curY2][curX2 + i] == 0:
                valuablePos.append({(curY1, curX1), (curY1, curX1 + i)})
                valuablePos.append({(curY2, curX2), (curY2, curX2 + i)})

    return valuablePos

def solution(board):

    N = len(board)
    newBoard = [[1] * (N+2) for _ in range(N+2)]

    for y in range(N):
        for x in range(N):
            newBoard[y+1][x+1] = board[y][x]

    q = deque()
    isVisited = []
    position = {(1,1),(1,2)}
    q.append((position,0))
    isVisited.append(position)

    while q:
        pos, value = q.popleft()

        if (N, N) in pos:
            return value

        for next_pos in checkValuablePos(pos, newBoard):
            if next_pos not in isVisited:
                q.append((next_pos, value +1))
                isVisited.append(next_pos)

    return 0


board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

print(solution(board))
