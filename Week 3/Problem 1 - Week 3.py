# Example 1

# 상하좌우 문제

# 여행가 A는 N X N 크기의 정사각형 공간 위에 서 있다. 이 공간은 1 X 1 크기의 정사각형으로 나누어져 있다. 가장 왼쪽 위 좌표는 (1, 1)이며,
# 가장 오른쪽 아래 좌표는 (N, N)에 해당한다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)이다.
# 여행가 A가 이동할 계획이 있는 계획서에는 하나의 줄에 띄어쓰기ㅡㄹㄹ 기준으로 하여 L, R, U, D 중 하나의 문자가 반복적으로 적혀 있다.
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동
# 이 때, A가 NXN 크기의 정사각형 공간을 벗어나는 움직임은 무시된다. 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시도니다.
# 계획서가 주어졌을 때 여행가 A가 최종적으로 도착할 지점의 좌표를 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 공간의 크기를 나타내는 N이 주어진다. (1<=N<=100)
# 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어진다. (1<=이동횟수<=100)
# 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백으로 구분하여 출력한다.

import sys

N = int(input())
map = sys.stdin.readline().rstrip().split()

begin = [1, 1]


for i in range(N):
    if map[i] == 'L':
        if begin[1] ==1:
            pass
        else :
            begin[1] -=1

    elif map[i] == 'R':
        if begin[1] == N :
            pass
        else:
            begin[1] +=1

    elif map[i] == 'U':
        if begin[0] == 1 :
            pass
        else:
            begin[0] -=1
    else:
        if begin[0] == N :
            pass
        else:
            begin[0] +=1


print(begin[0], begin[1])

# Another solution

N = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]

        if nx<1 or ny<1 or nx>n or ny>n:
            continue
        x, y = nx, ny

print(x, y)