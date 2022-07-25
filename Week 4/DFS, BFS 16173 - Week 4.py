# 백준 16173 (점프왕 쩰리)

# 문제

# '쩰리'는 점프하는 것을 좋아하는 젤리다. 단순히 점프하는 것에 지루함을 느낀 '쩰리'는 새로운 점프 게임을 해보고 싶어 한다.
# 새로운 점프 게임의 조건은 다음과 같다.

# 1. '쩰리'는 가로와 세로의 칸 수가 같은 정사각형의 구역 내부에서만 움직일 수 있다. '쩰리'가 정사각형 구역의 외부로 나가는 경우엔
# 바닥으로 떨어져 즉시 게임에서 패배하게 된다.
# 2. '쩰리'의 출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다. 다른 출발점에서는 출발하지 않는다.
# 3. '쩰리'가 이동 가능한 방향은 오른쪽과 아래 뿐이다.
# 4. '쩰리'가 가장 오른쪽, 가장 아래 칸에 도달하는 순간, 그 즉시 '쩰리'의 승리로 게임은 종료된다.
# 5. '쩰리'가 한 번에 이동할 수 있는 칸의 수는, 현재 밟고 있는 칸에 쓰여 있는 수 만큼이다.
# 칸에 쓰여 있는 수 초과나 그 미만으로 이동할 수 없다.

# 새로운 게임이 맘에 든 '쩰리'는, 계속 게임을 진행해 마침내 최동 단계에 도달했다. 하지만, 게임을 진행하는 구역이 너무 넓어져버린 나머지
# 이 게임에서 이길 수 있는지 없는지 가늠할 수 없어졌다.
# 쩰리를 도와 주어진 게임 구역의 끝 점까지 도달할 수 있는지를 알아보자

# 입력 : 입력의 첫 번째 줄에는 게임 구역의 크기 N(2<=N<=3)이 주어진다.
# 입력의 두 번째 줄부터 마지막 줄까지 게임판의 구역이 주어진다.
# 게임판의 승리 지점에는 -1이 쓰여있고, 나머지 칸에는 0 이상 100 이하의 정수가 쓰여 있다.

# 출력 : '쩰리가' 끝 점에 도달할 수 있으면 'HaruHaru'를, 도달할 수 없으면 'Hing'을 한 줄에 출력한다.

import sys
from collections import deque

N = int(input())

land = []
for _ in range(N):
    land.append(list(map(int, sys.stdin.readline().split())))




def jumping(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0]*N for _ in range(N)]

    while q:

        x, y = q.popleft()
        length = land[x][y]
        nx = x+length
        ny = y+length

        if x==N-1 and y==N-1:
            break

        if nx<N and visited[nx][y]==0:
            q.append((nx, y))
            visited[nx][y]=1
        if ny<N and visited[x][ny]==0:
            q.append((x, ny))
            visited[x][ny]=1


    if land[x][y]==-1:
        return('HaruHaru')
    else:
        return('Hing')


print(jumping(x=0, y=0))

# point : 중복해서 왔다갔다하면 안된다 - 메모리나 시간 초과 발생할 수 있음
# 그래서 visited 함수 사용해서 내가 간 곳을 체크해주어야 함.