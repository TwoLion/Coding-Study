# 문제

# 동네 편의점의 주인인 동빈이는 N개의 동전을 가지고 있습니다.
# 이때 N개의 동전을 이용하여 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램을 작성하세요.

from itertools import combinations

N = int(input())
a = list(map(int, input().split()))

result = []

for i in range(1, len(a)+1):
  result += list(map(sum, list(combinations(a, i))))

result = set(result)

comp = set(range(1, sum(a)+2))

print(min(comp - result))

# 다시 풀기 아이디어


import sys

N = int(input())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
result = 1

for i in a:
  if result < i :
    break
  else:
    result += i

print(result)