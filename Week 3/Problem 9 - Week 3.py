# 문제 Q11

# 문제

# Dummy라는 도스 게임이 있습니다. 이 게임에는 뱀이 나와서 기어 다니는데, 사과를 먹으면 뱀 길이가 늘어납니다.
# 뱀이 이리저리 기어 다니다가 벽 또는 자기 자신의 몸과 부딪히면 게임이 끝납니다.
# 게임은 N x N 정사각 보드 위에서 진해오디고, 몇몇 칸에는 사과가 놓여져 있습니다. 보드의 상하좌우 끝에는 벽이 있습니다.
# 게임을 시작할 때 뱀은 맨 위 맨 좌측에 위치하고 뱀의 길이는 1입니다.
# 뱀은 처음에 오른쪽을 향합니다.
# 뱀은 매 초마다 이동을 하는데 다음과 같은 규칙을 따릅니다.

# 먼저 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킵니다.
# 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않늣ㅂ니다.
# 만약 이동한 칸에 사과가 없다면, 몸길이를 불여서 꼬리가 위치한 칸을 비워줍니다. 즉, 몸길이는 변하지 않습니다.

# 사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하세요.

# 입력 : 첫째 줄에 보드의 크기 N이 주어집니다.(2<=N<=100) 다음 줄에 사과의 개수 K개 주어집니다.(2<=K<=100)
# 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미합니다. 사과의 위치는
# 모두 다르며, 맨 위 맨 좌측 (1행 1열)에는 사과가 없습니다.
# 다음 줄에는 뱀의 방향 변환 횟수 L이 주어집니다. (1<=L<=100)
# 다음 L개의 줄에는 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며, 게임 시작 시간으로부터
# X초가 끝난 뒤에 왼쪽 (C가 'L') 또는 오른쪽(C가 'D')으로 90도 방향을 회전시킨다는 뜻입니다. X는 10000 이하의 정수이며,
# 방향 전환 정보는 X가 증가하는 순으로 주어집니다.

# 출력 : 첫째 줄에 게임이 몇 초에 끝나는지 출력합니다.


import sys

N = int(input())
K = int(input())

apple =[]

for _ in range(K):
    apple.append(list(map(int, sys.stdin.readline().split())))

L = int(input())

direction = []

for i in range(L):
    direction.append(sys.stdin.readline().split())
    direction[i][0] = int(direction[i][0])




#방향 설정 : 북, 서, 남, 동
D = ['N', 'W', 'S', 'E']
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 뱀 움직이는 함수
# 움직인 뱀 머리 위치를 이전 뱀에 추가한 뒤, 만약 사과가 없으면 꼬리 부분을 잘라냄
# 벽에 부딪히거나, 자기 몸에 부딪히는 경우 result =1 반환
def moving(snake, apple, dire, M):

    next_head = [snake[0][0]+dx[D.index(dire)], snake[0][1]+dy[D.index(dire)]]

    new_snake = [next_head]+snake

    if next_head in apple:
        pass
    else:
        new_snake.pop(-1)

    if next_head[0]>M or next_head[1]>M or next_head[0]<1 or next_head[1]<1 or next_head in snake:
        result = 1
    else:
        result = 0

    return(new_snake, result, snake)

# 방향 바꾸는 함수
# 방향 바꾸는 시간이 움직인 시간과 같은 경우 작동

def change_direction(now_dire, now_time, change_time, change_dire):

    if now_time!=change_time:
        return(now_dire)

    else:
        if change_dire == 'L':
            return(D[D.index(now_dire)-3])
        else :
            return(D[D.index(now_dire)-1])


# 시간:
Time = 0
# 현재 방향:
d = 'E'
# 출발지점
snake=[[1, 1]]
# 사과
apple
# 방향 전환 시간
direction

# result가 1이 될때까지 이동 후 방향전환 반복

while True:


    result = moving(snake = snake, apple = apple, dire = d, M=N)
    if result[1]==1:
        Time +=1
        break

    snake = result[0]
    if snake[0] in apple:
        apple.remove(snake[0])

    Time +=1
    if len(direction)!=0:
        newd = change_direction(now_dire = d, now_time=Time, change_time = direction[0][0], change_dire=direction[0][1])

    if newd!=d:
        direction.pop(0)
    d = newd


print(Time)