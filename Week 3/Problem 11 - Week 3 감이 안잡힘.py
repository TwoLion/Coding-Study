# Q13 백준 15686(치킨 배달)

# 문제

# 크기가 N x N인 도시가 있습니다. 도시는 1 x 1 크기의 칸으로 나누어져 있습니다. 도시의 각 칸은 빈칸, 치킨집, 집 중 하나입니다.
# 도시의 칸은 (r, c)와 같은 형태로 나타내고, r행 c열 또는 위에서부터 r번째 칸, 왼쪽에서부터 c번째 칸을 의미합니다. r과 c는 1부터
# 시작합니다.

# 이 도시에 사는 사람들은 치킨을 매우 좋아합니다. 따라서 사람들은 '치킨 거리'라는 말을 주로 사용합니다. 치킨 거리는 집과 가장 가까운
# 치킨집 사이의 거리입니다. 즉, 치킨 거리는 집을 기준으로 정해지며, 각각의 집은 치킨 거리를 가지고 있습니ㅏㄷ.
# 도시의 치킨 거리는 모든 집의 치킨 거리의 합입니다.
# 임의의 두칸 (r_1, c_1)과 (r_2, c_2)사이의 거리는 |r_1-r_2| +|c_1-c_2|로 구합니다.
# 이 도시에 있는 치킨집은 모두 같은 프랜차이즈입니다. 프렌차이즈 본사에서는 수익을 증가시키기 위해 일부 치킨집을 폐업시키려고 합니다.
# 오랜 연구 끝에 이 도시에서 가장 수익을 많이 낼 수 있는 치킨집의 개수는 최대 M개라는 사실을 알아냈습니다.
# 도시에 있는 치킨집 중에서 최대 M개를 고르고, 나머지 치킨집은 모두 폐업시커야 합니다. 어떻게 고르면, 도시의 치킨거리가 가장
# 작게 될지 구하는 프로그램을 작성하세요.

# 입력 : 첫째 줄에 N(2<=N<=50)과 M(1<=M<=13)이 주어집니다.
# 둘째 줄부터 N개의 줄에는 도시의 정보가 주어집니다.
# 도시의 정보는 0, 1, 2로 이루어져 있고, 0은 빈칸, 1은 집, 2는 치킨집을 의미합니다. 집의 개수는 2N개를 넘지 않으며, 적어도
# 한개는 존재합니다. 치킨집의 개수는 M보다 크거나 같고, 13보다 작거나 같습니다.

# 출력 : 첫째 줄에 폐업시키지 않을 치킨집을 최대 M개를 골랐을 때, 도시의 치킨 거리의 최솟값을 출력합니다.


import sys
from itertools import combinations


N, M = map(int, sys.stdin.readline().split())


# 전체 지도를 부를 필요 없이 집과 치킨집의 위치만 불러오기

house = []
chick = []


for i in range(1, N+1):
    land = list(map(int, sys.stdin.readline().split()))

    for j in range(len(land)):
        if land[j]==1:
            house.append([i, j+1])
        elif land[j]==2:
            chick.append([i, j+1])
        else:
            pass

# 치킨 거리 정의

def dist(house, chick_list):

    chick_dist = list(map(lambda x: abs(house[0]-x[0])+abs(house[1]-x[1]), chick_list))

    result =[]
    for i in range(len(chick_list)):
        result.append([chick_list[i], chick_dist[i]])

    return(result)


def chick_dist(house_list, chick_list):

    result = []

    for i in range(len(house_list)):
        distance = dist(house = house_list[i], chick_list=chick_list)
        distance.sort(key = lambda x: x[1])
        result.append(distance[0])
        result.sort(key = lambda x: x[1])

    return(result)






# M개의 모든 치킨 집 조합에 대해서 전체 치킨거리 구하기.


chick_case = list(combinations(chick, M))
final = []
for i in range(len(chick_case)):
    city_dist_case=0
    case_dist = chick_dist(house_list=house, chick_list = chick_case[i])
    for j in range(len(case_dist)):

        city_dist_case += case_dist[j][1]

    final.append(city_dist_case)

print(min(final))


