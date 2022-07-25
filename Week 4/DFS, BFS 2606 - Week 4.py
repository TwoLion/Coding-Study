# 백준 2606(바이러스)

# 신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는
# 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해
# 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번부터 차례대로 번호가 매겨진다.
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 텀퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서
# 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

# 출력 : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

import sys
from collections import deque

N = int(input())
M = int(input())

line =[]

for _ in range(M):
    line.append(list(map(int, sys.stdin.readline().split())))


def virus(line):

    q =deque()
    q.append(1)
    visited=[0]*(N+1)
    while q:

        first = q.popleft()

        for i in range(len(line)):
            if line[i][0]==first and visited[line[i][1]]==0:
                q.append(line[i][1])
                visited[line[i][1]]=1

            if line[i][1]==first and visited[line[i][0]]==0:
                q.append(line[i][0])
                visited[line[i][0]]=1

    return(sum(visited)-1)

print(virus(line=line))