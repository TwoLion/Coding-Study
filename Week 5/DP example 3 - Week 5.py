# 효율적인 화폐구성

# 문제

# N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
# 이때 각 화폐는 몇 개라도 사용할 수 잇으며, 사용한 화폐의 구성은 같지만 순서만 다른 것은 같은 경우로 구분한다.
# 예를 들어 2원, 3원 단위의 화페가 있을 때는 15원을 만들기 위해 3원을 5개 사용하는 것이 가장 최소한의 화폐 개수이다.

# 입력 : 첫째 줄에 N, M이 주어진다.
# 이후 N개의 줄에는 각 화폐의 가치가 주어진다. 화폐 가치는 10,000보다 작거나 같은 자연수이다.

# 출력 : 첫째 줄에 M원을 만들기 위한 최소한의 화폐 개수를 출력한다.
# 불가능할 때는 -1을 출력한다.

import sys
N, M = map(int, input().split())

money = []
for _ in range(N):
    money.append(int(sys.stdin.readline()))

money.sort()
d = [10001]*10001

for i in money:
    d[i]=1



for i in range(1, M+1):
    for j in money:
        if i>=j:
            d[i] = min(d[i-j]+1, d[i])


if d[M]==10001:
    print(-1)
else:
    print(d[M])