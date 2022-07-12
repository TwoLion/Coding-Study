# 문제
# 각 자리가 숫자 (0부터 9)로만 이루어진 문자열 S가 주어졌을 때,
# 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 혹은 '+' 연산자를 넣어
# 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.



# 입력 조건 : 첫째 줄에 여러 개의 숫자로 구성된 하나의 문자열 S가 주어집니다.
# 출력 조건 : 첫째 줄에 만들어질 수 있는 가장 큰 수를 출력합니다.


a = input()

b = []
result = 1

for i in range(len(a)):
  b.append(a[i])

b = list(map(int, b))

while 0 in b :
  b.remove(0)


for i in range(len(b)):
  result *= b[i]

print(result)

# 알아야 할 함수
# list 원소 모두 더하거나 곱해주는 함수
# 더해주는 함수 : sum
# 붙어있는 문자 모두 seperate해주는 함수
# 특정 값 모두 없애주는 함수

# reduce 함수 이용해보기
# reduce(function, sequence(, initial))
# : function을 sequence 순서대로 연산을 해주는 함수

from functools import reduce

def multiply(arr):
  return reduce(lambda x, y: x*y, arr)

print(multiply(arr = b))


# 붙어있는 문자 모두 seperate해주는 함수 : string에 list 붙이면 됩니다.

print(list(a))

# remove all 해주는 함수 : set 이용하기

b = list(map(int, input().split()))
r = set([0])

b = [i for i in b if i not in r]

print(b)

# Another solution

from functools import reduce

a = map(int, list(input()))

zero_set = set([0])


a = [i for i in a if i not in zero_set]

def multiply(arr):
  return reduce(lambda x, y: x*y, arr)

print(multiply(a))


# 더하기, 곱하기 결과 비교해서 큰 값만 살리기 vs 1, 0 고려해서 식 짜보기.
# 틀린 이유 : 1을 고려하지 않음 : 1인 경우 더해주어야 함.

a = list(map(int, list(input())))

result = a[0]

for i in range(1, len(a)):

  if a[i]<=1 or result<=1:
    result += a[i]
  else:
    result *= a[i]

print(result)

# another solution

a = list(map(int, list(input())))

result =a[0]

for i in range(1, len(a)):

  result = max(result*a[i], result+a[i])


print(result)