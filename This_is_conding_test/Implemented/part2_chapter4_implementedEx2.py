
# 15 minutes
#
# 4 4
# 1 1 0
# 1 1 1 1
# 1 0 0 1
# 1 1 0 1
# 1 1 1 1

# 하... 훨씬 간단히 할 수 있었다.. Ex1처럼 ㅠㅠ
# 컨셉은 맞게 한거 같다.
# 근데 뒤로 빽하거나 이동할때 왜 map 크기 조건은 안따지지??

N, M = map(int,input().split())
x,y,head = map(int, input().split())

nx = x
ny = y
# head = 0, 1, 2, 3 --> 북 동 남 서


game = [[0 for cols in range(4)] for rows in range(4)]

for i in range(0,M):
    game[i][:] = map(int, input().split())

# print(game)

canMove = 0
isthereLand = 4

game[ny][nx] = 2            # 시작이 땅이라고 했으니까 내가 시작한 땅은 밟은것??
countLand = 1
# print("head : %d" %head)
while canMove == 0:
    # 먼저 head를 반시계방향으로 회전

    # print("head : %d" % head)
    if head -1 < 0:
        head = 3
    else:
        head -= 1

    if isthereLand == 0:        # 모두 가봤거나 바다인 경우
        print("hi")
        isthereLand = 4
        head += 1               # head를 원래 대로 유지
        print(head)
        if head == 0:
            if ny + 1 > 0 and game[ny + 1][nx] != 1:
                ny = ny - 1  # 이동
                continue
            else:
                canMove = 1
                continue
        if head == 1:
            if nx - 1 < N and game[ny][nx - 1] != 1:  # 동
                nx = nx - 1  # 이동
            else:
                canMove = 1
                continue
        if head == 2:
            if ny - 1 < M and game[ny - 1][nx] != 1:  # 남
                ny = ny - 1  # 이동
                continue
            else:
                canMove = 1
                continue
        if head == 3:
            if nx + 1 > 0 and game[ny][nx + 1] != 1:  # 서
                nx = nx + 1  # 이동
                continue
            else:
                canMove = 1
                continue

    # 4방향 모두 check 하는 로직
    # 바꾼 방향이 북쪽이면서 map을 벗어나면 안되고, 육지이며 , 방문하지 않은 경우

    if head == 0:
        print("head 0")
        if ny - 1 > 0 and game[ny-1][nx] == 0 and game[ny-1][nx] != 2:
            print("head 0-1")
            game[ny-1][nx] = 2          # 이동 표시 : 2
            ny = ny - 1                 # 이동
            countLand += 1
            isthereLand = 4
            continue
        else:
            print("head 0-2")
            isthereLand -= 1
            continue
    if head == 1:
        print("head 1")
        if nx + 1 < N and game[ny][nx+1] == 0 and game[ny][nx+1] != 2:             # 동
            print("head 1-1")
            game[ny][nx+1] = 2          # 이동 표시 : 2
            nx = nx + 1                 # 이동
            countLand += 1
            isthereLand = 4
            continue
        else:
            print("head 1-2")
            isthereLand -= 1
            continue
    if head == 2:
        print("head 2")
        if ny + 1 < M and game[ny+1][nx] == 0 and game[ny+1][nx] != 2:          # 남
            print("head 2-1")
            game[ny+1][nx] = 2          # 이동 표시 : 2
            ny = ny + 1                 # 이동
            isthereLand = 4
            countLand += 1
            continue
        else:
            print("head 2-2")
            isthereLand -= 1
            continue
    if head == 3:
        print("head 3")
        if nx -1 > 0 and game[ny][nx -1] == 0 and game[ny][nx - 1] != 2:          # 서
            print("head 3-1")
            game[ny][nx-1] = 2         # 이동 표시 : 2
            nx = nx - 1                 # 이동
            isthereLand = 4
            countLand += 1
            continue
        else:
            print("head 3-2")
            isthereLand -= 1
            continue





print(countLand)