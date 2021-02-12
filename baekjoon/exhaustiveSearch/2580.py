import sys


input = sys.stdin.readline

sudoku = [list(map(int,input().split()) for _ in range(9))]

numList = [0,1,2,3,4,5,6,7,8,9]

def dfs(x, y, size):
    if size == 1:
        x_axisList = sudoku[y][:]
        y_axisList = sudoku[:][x]
        for i in range(9):
            if i not in x_axisList and i not in y_axisList:
                sudoku[y][x] = i

        return
    elif size == 3:
        cnt = 0
        for y in range(y, size):
            for x in range(x, size):
                numList[sudoku[y][x]] += 1
                if sudoku[y][x] == 0:
                    cnt += 1
        if cnt == 1:
            for i in range(1,11):
                if numList[i] == 0:
                    sudoku[y][x] = i
            return
        else:
            dfs(x)




    for y in range(y, size, size // 3):
        for x in range(x, size, size // 3):
            dfs(x, y, size // 3)










