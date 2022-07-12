# 문제
# 한 마을에 모험가가 N명 있습니다. N명의 모험가를 대상으로 '공포도'를 측정했는데,
# '공포도'가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서 제대로 대처할 능력이 떨어집니다.
# 모험가 길드장인 동빈이는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는
# 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 여행을 떠날 수 있도록 규정했습니다.
# 또한 몇 명의 모험가는 마을에 그대로 남아 있어도 되기 때문에, 모든 모험가를 특정한 그룹에 넣을 필요는 없습니다.

# 동빈이를 위해 N명의 모험가에 대한 정보가 주어졌을 때, 여행을 떠날 수 있는 그룹 수의 최댓값을 구하는 프로그램을 작성하시오.

# 입력 조건 : 첫째 줄에 모험가의 수 N이 주어집니다.
# 둘째 줄에 각 모험가의 공포도의 값을 N 이하의 자연수로 주어지며, 각 자연수는 공백으로 구분합니다.
# 여행을 떠날 수 있는 그룹 수의 최댓값을 출력합니다.

N = int(input())
traveler = list(map(int, input().split()))

traveler.sort(reverse=True)
count = 0

for _ in range(N):
  num = traveler[0]
  traveler = traveler[num:]
  count +=1
  if traveler[0] == len(traveler):
    count +=1
    break
  elif traveler[0] > len(traveler):
    break
  else:
    pass

print(count)


### 틀렸음 - 최대부터 진행하면, 1, 1, 1, 8과 같은 경우는 제외됨 - 따라서 최소부터 진행해야 함

import sys

N = int(input())
traveler = list(map(int, sys.stdin.readline().split()))

result = 1
count = 0
traveler.sort()


for i in traveler:
  if result >= i :
    result = 1
    count += 1
  else:
    result +=1

print(count)

