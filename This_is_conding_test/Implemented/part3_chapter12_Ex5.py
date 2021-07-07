# https://www.acmicpc.net/problem/3190
# 하....
# 접근은 괜찮았는데 코드 구현이 많이 복잡했다 
# 더 간결하게 작성할 수 있었을텐데
# 그나저나 예제가 이해가 안간다 ㅡㅡ
# 음... 다시 손봐야할듯..




N = int(input())            # 맵의 크기
K = int(input())            # 사과의 갯수

mapInfor = [[0] * N for _ in range(N)]      # N x N map


for i in range(K):
    y, x = map(int,input().split())
    mapInfor[y-1][x-1] = 1                      # 사과 위치 갱신

L = int(input())            # 뱀의 방향 변환 횟수

dx = [ 1, -1, 0, 0]            # 동서남북
dy = [ 0, 0, 1, -1]

snakePosition = [(0,0)]
snakeHeading = [1,0]                           # 뱀의 머리 방향 초기 동쪽 (dx[0] dy[0])

totalTime = 0

def checkCrashSelf(snakePosition,x,y):

    for i in range(0, len(snakePosition)):
        snakeX, snakeY = snakePosition[i][0], snakePosition[i][1]
        if snakeX == x and snakeY == y:
            return True

    return False


time, head = input().split()        # 뱀의 방향 횟수 입력

isCrashed = False
while True:
    totalTime += 1
    x = snakePosition[len(snakePosition) -1][0] + snakeHeading[0]                   # 위치 갱신
    y = snakePosition[len(snakePosition) -1][1] + snakeHeading[1]

    if x < len(mapInfor) and y < len(mapInfor[0]) and x > -1 and y > -1 and checkCrashSelf(snakePosition,x,y) == False:

        if mapInfor[y][x] == 1:                             # 사과가 있다면
            mapInfor[y][x] = 0                              # 사과를 먹어버리고
            snakePosition.append((x,y))
        else:                                               # 사과가 없다면
            snakePosition.append((x,y))
            del snakePosition[0]
    else:
        isCrashed = True
        print(totalTime)
        break

    # time동안 다 돌았으면 방향 갱신
    if totalTime == int(time):
        if head == "D":  # 만약 오른쪽이면
            if snakeHeading[0] == 1 and snakeHeading[1] == 0:  # 동 -> 남
                snakeHeading[0], snakeHeading[1] = dx[2], dy[2]
            elif snakeHeading[0] == -1 and snakeHeading[1] == 0:  # 서 -> 북
                snakeHeading[0], snakeHeading[1] = dx[3], dy[3]
            elif snakeHeading[0] == 0 and snakeHeading[1] == 1:  # 남 -> 서
                snakeHeading[0], snakeHeading[1] = dx[1], dy[1]
            else:  # 북 -> 동
                snakeHeading[0], snakeHeading[1] = dx[0], dy[0]
        else:  # 만약 왼쪽이면
            if snakeHeading[0] == 1 and snakeHeading[1] == 0:  # 동 -> 북
                snakeHeading[0], snakeHeading[1] = dx[3], dy[3]
            elif snakeHeading[0] == -1 and snakeHeading[1] == 0:  # 서 -> 남
                snakeHeading[0], snakeHeading[1] = dx[2], dy[2]
            elif snakeHeading[0] == 0 and snakeHeading[1] == 1:  # 남 -> 동
                snakeHeading[0], snakeHeading[1] = dx[0], dy[0]
            else:  # 북 -> 서
                snakeHeading[0], snakeHeading[1] = dx[1], dy[1]





