# https://programmers.co.kr/learn/courses/30/lessons/60061

n = int(input())


# x, y, a, b
# a : 설치 또는 삭제할 구조물, 0은 기둥 1은 보
# b : 설치할것인가 삭제할것인가. 삭제 0 설치 1

build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]



def install(mapLocation, x,y,a):

    isPossible = False

    if a == 0: #기둥 설치
        if y > -1 and y < len(mapLocation) -1:
            if mapLocation[y][x-1] == 2 or mapLocation[y-1][x] == 1:          # 바닥위에 있거나 보의 한쪽 긑 부분 위에 있거나 또다른 기둥 위에 있어야한다.
                isPossible = True
    else:       # 보 설치
        if x > -1 and x < len(mapLocation) -1:
            if mapLocation[y-1][x] == 1 or mapLocation[y-1][x+1] == 1:          # 보의 한쪽 끝 부분이 기둥인경우
                isPossible = True
            elif mapLocation[y][x-1] == 2 and mapLocation[y][x+1] == 2:         # 보의 양쪽 끝 부분이 다른 보와 동시에 연결되는 경우
                isPossible = True

    return isPossible

def delete(mapLocation, x,y,a):

    isPossible = True

    if a == 0:  # 기둥 설치
        if mapLocation[y + 1][x] == 2 or mapLocation[y + 1][x] == 1 or mapLocation[y - 1][x] == 1:  # 바닥위에 있거나 보의 한쪽 긑 부분 위에 있거나 또다른 기둥 위에 있어야한다.
            isPossible = True
    else:  # 보 삭제
        if mapLocation[y - 1][x] == 1 or mapLocation[y][x + 1] == 2:  # 보의 왼쪽 부분이 기둥이면서 다른 한쪽은 보인경우
            isPossible = False
        elif mapLocation[y - 1][x + 1] == 1 or mapLocation[y][x - 1] == 2:  # 보의 오른쪽 끝 부분이 기둥이면서 다른 한쪽은 보인경우
            isPossible = False
        elif mapLocation[y][x - 1] != 2 and mapLocation[y][x + 1] != 2 and mapLocation[y - 1][x] != 1:  # 혹시 보들 사이의 중간이면서 기둥이 없는 경우 #바닥에 보를 설치하는 경우는 없으므로 y 조건 생략
            isPossible = False

    return isPossible

def solution(n, build_frame):
    mapLocation = [[0] * (n + 1) for _ in range(n + 1)]
    answer = []
    for build in build_frame:
        x, y, a, b = build[0],build[1],build[2],build[3]

        if b == 0: # 삭제
            if a == 0:  #기둥
                isPossible = delete(mapLocation, x,y,a)
                if isPossible == True:
                    answer.delete((x,y,a))
            else:       # 보
                isPossible = install(mapLocation, x,y,a)
                if isPossible == True:
                    answer.delete((x,y,a))

        else:       # 설치
            if a == 0:  #기둥
                isPossible = install(mapLocation, x,y,a)
                if isPossible == True:
                    answer.append((x,y,a))
            else:       # 보
                isPossible = install(mapLocation, x,y,a)
                if isPossible == True:
                    answer.append((x,y,a))


    # answer((x,y,a))   # 각 구조물의 좌표(x,y), 기둥 or 보 # x 좌표 기준으로 오름차순 -> y좌표 기준으로 오름차순 -> 둘다 같으면 기둥기준으로 오름차순