
# 15 minutes

position = list(input())

x,y = int(ord(position[0]) - 96), int(position[1])

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

cnt = 0
for i in range(0,8):
    nx = x + dx[i]
    ny = y + dy[i]
    # print(nx,ny)
    if nx > 0 and nx < 9 and ny > 0 and ny < 9:
       cnt += 1

# print(x,y)
print(cnt)
