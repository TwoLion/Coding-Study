# 백준 18111

# 문제

# 팀 레드시프트는 대회 준비를 하다가 지루해져서 샌드박스 게임인 '마인크래프트'를 켰다. 마인크래프트는 1X 1X 1 크기의 블록들로 이루어진
# 3차원 세계에서 자유롭게 땅을 파거나 집을 지을 수 있는 게임이다.

# 목재를 충분히 모은 lvalue는 집을 짓기로 하였다. 하지만 고르지 앟은 따엥는 집을 지을 수 없기 때문에 땅의 높이를 모두 동일하게 만드는
# 땅 고르기 작업을 해야한다.

# lvalue는 세로 N, 가로 M 크기의 집터를 골랐다. 집터 맨 왼쪽 위의 좌표는 (0, 0)이다. 우리의 목적은 이 집터 내의 땅의 높이를 일정하게
# 바꾸는 거이다. 우리는 다음과 같은 두 종류의 작업을 할 수 있다.

# 1. 좌표 (i, j)의 가장 위에 있는 블록을 제거하여 인벤토리에 넣는다.
# 2. 인벤토리에서 블록 하나를 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓는다.

# 1번 작업은 2초가 걸리며, 2번 작업은 1초가 걸린다. 밤에는 무서운 몬스터들이 나오기 때문에 최대한 빨리 땅 고르기 작업을 마쳐야 한다.
# 땅 고르기 작업에 걸리는 최소 시간과 그 경우 땅의 높이를 출력하시오.

# 단ㄴ, 집터 아래에 동굴 등 빈 공간은 존재하지 않으며, 집터 바깥에서 블록을 가져올 수 없다. 또한, 작업을 시작할 때 인벤토리에는 B개의
# 블록이 들어 있다. 땅의 높이는 256블록을 초과할 수 없으며, 음수가 될 수 없다.

# 입력

# 첫째 줄에 N, M, B가 주어진다. (1<=M, N<=500, 0<=B<=6.4X10^7)
# 둘째 줄부터 N개의 줄에 각각 M개의 정수로 땅의 높이가 주어진다. (i+2)번째 줄의 (j+1)번째 수는 좌표 (i, j)에서의 땅의 높이를 나타낸다.
# 땅의 높이는 256보다 작거나 같은 자연수 또는 0이다.

# 출력

# 첫째 줄에 땅을 고르는 데 걸리는 시간과 땅의 높이를 출력하시오. 답이 여러 개 있다면 그중에서 땅의 높이가 가장 높은 것을 출력하시오.

import sys


N, M, B = map(int, sys.stdin.readline().split())


result = []

for _ in range(N):
    land = list(map(int, sys.stdin.readline().split()))
    result += land


count = [0]*(max(result)+1)
floor = range(max(result)+1)
for i in result:
    count[i] +=1

# land : 층마다 블록 개수
# floor : 층 설명 해주는 지표
# need : 만들 층

# block 개수와 시간 도출

def making_land(land, floor, need):

    floor_block = list(map(lambda x: need-x, floor)) #해당 층을 만드는데 층마다 필요한 블록 개수
    need_block = [i*j for i, j in zip(floor_block, land)] # 존재하는 해당 층까지 고려하여 필요한 블록 개수

    count = sum(need_block)
    time = 0
    for i in need_block:
        if i<0:
            time +=2*abs(i)
        else:
            time +=abs(i)

    return([time, count])


final_result = []
for i in floor:

    case = making_land(land=count, floor=floor, need=len(floor)-i-1)

    if case[1]>B:
        continue

    final_result.append(case+[len(floor)-i-1])

final_result.sort(key = lambda x: (x[0], -x[2]))

print(final_result[0][0], final_result[0][2])



