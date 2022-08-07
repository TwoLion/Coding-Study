# 문제

# 어떤 나라에는 1번부터 N번까지의 도시와 M개의 단방향 도로가 존재한다. 모든 도로의 거리는 1이다.

# 이 때 특정한 도시 X로부터 출발하여 도달할 수 있는 모든 도시 중에서,
# 최단 거리가 정확히 K인 모든 도시들의 번호를 출력하는 프로그램을 작성하시오.
# 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

# 입력

# 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
# (2 ≤ N ≤ 300,000, 1 ≤ M ≤ 1,000,000, 1 ≤ K ≤ 300,000, 1 ≤ X ≤ N)
# 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 공백을 기준으로 구분되어 주어진다.
# 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미다.
# (1 ≤ A, B ≤ N) 단, A와 B는 서로 다른 자연수이다.


import sys
import heapq

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

city = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    city[a].append((1, b))


INF = int(1e9)

distance = [INF]*(N+1)

# 디엑스트라 알고리즘 이용 최단거리 구하기

def dextra(start):
    q = []
    distance[start] =0
    heapq.heappush(q, (0, start))

    while q:
        dist, now = heapq.heappop(q)

        if distance[now]<dist:
            continue
        for i in city[now]:
            cost = dist + i[0]
            if distance[i[1]]> cost:
                distance[i[1]]=cost
                heapq.heappush(q, (cost, i[1]))



dextra(start = X)

# 최단거리가 K가 없으면 -1 출력, K가 있으면 최단거리가 K인 인덱스 출력

if K not in distance:
    print(-1)

else:
    for i in range(len(distance)):
        if distance[i]==K:
            print(i)
