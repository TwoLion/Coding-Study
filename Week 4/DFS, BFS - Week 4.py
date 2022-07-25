# 재귀함수 팩토리얼 구현 예제

# 반복적으로 구현한 n!

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *=i
    return(result)


# 재귀함수로 구현한 n!

def factorial_recursive(n):
    if n<=1:
        return 1
    return(n*factorial_recursive(n-1))

print('반복 구현', factorial_iterative(5))
print('재귀함수 구현', factorial_recursive(5))


# 재귀함수 최대공약수 계산

# 유클리드 호제법
# A를 B로 나눈 나머지를 R
# A와 B의 최대공약수는 A와 R의 최대공약수와 같음

def gcd(a, b):
    if a % b ==0:
        return b
    else:
        return(gcd(b, a%b))

print(gcd(192, 162))


# DFS 예제

# 각 노드가 연결된 정보를 표현

graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

# 각 노드가 방문된 정보를 표현

visited = [False]*9 # index 0은 제외함

# DFS method 정의

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


dfs(graph, 1, visited)


# BFS method 정의

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph, start=1, visited=visited)