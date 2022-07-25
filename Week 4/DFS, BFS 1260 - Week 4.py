# 백준 1260 (DFS와 BFS)

# 문제

# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더이상 방문할 수 있는 점이 없는
# 경우에는 종료한다. 점검 번호는 1번부터 N번까지이다.

# 입력

# 첫째 줄에 정점의 개수 N(1<=N<=1000), 간선의 개수 M(1<=M<=10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다.
# 입력으로 주어지는 간선은 양방향이다.

# 출력

# 첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.

from collections import deque

N, M, V = map(int, sys.stdin.readline().split())

line =[]
for _ in range(M):
    line.append(list(map(int, sys.stdin.readline().split())))

line.sort()


stack = []

visited = [0]*(N+1)



def dfs(line, V):

    stack.append(V)

    visited[V]=1


    for i in range(M):
        if line[i][0] ==V and visited[line[i][1]]==0:
            dfs(line=line, V=line[i][1])


        if line[i][1]==V and visited[line[i][0]]==0:
            dfs(line=line, V=line[i][0])






def bfs(line, V):

    q = deque()
    q.append(V)

    number = [0]*(N+1)
    number[V]=1

    result = []

    while q:

        check = q.popleft()

        result.append(check)

        for i in range(M):
            if check == line[i][0] and number[line[i][1]]==0:
                q.append(line[i][1])
                number[line[i][1]]=1

            if check == line[i][1] and number[line[i][0]]==0:
                q.append(line[i][0])
                number[line[i][0]]=1


    return(result)


dfs(line, V)


print(*stack)


print(*bfs(line = line, V=V))