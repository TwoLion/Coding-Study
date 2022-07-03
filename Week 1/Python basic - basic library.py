# 표준 라이브러리

# 내장 함수 : 기본 입출력 함수부터 정렬 함수까지 기본적인 함수들을 제공
#   - 파이썬 프로그램을 작성할 때 없어서는 안 되는 필수적인 기능 포함
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
#   - 순열과 조합 라이브러리
# heapq : 힙(Heqp) 자료구조 제고
#   - 일반적으로 우선순위 큐 기능을 구현하기 위해 사용
# bisect : 이진탑색(binary search) 기능 제공
# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조 포함
# math : 필수적인 수학적 기능 제공
#   - 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수부터 파이(pi)와 같은 상수 포함


################################################################################

# 내장 함수

#sum()

result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)

print(min_result, max_result)

# eval()

result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
    return x[1]

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))


#############################################################################

# itertool

# 순열 : 서로 다른 n개에서 r개를 선택하여 일렬로 나열하는 것
# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것

# 순열

from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 2))
print(result)

# 조합

from itertools import combinations
data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)

# 중복 순열

from itertools import product

data = ['A', 'B', 'C']
result = list(product(data, repeat = 2))
print(result)

# 중복 조합

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
result = list(combinations_with_replacement(data, 2))
print(result)

############################################################################################

# Counter

# Counter : 등장 횟수를 세는 기능 제공
# 리스트와 같은 반복 간으한 객체가 주어졌을 때 내부의 원소가 몇 번씩 등장했는지를 알려줌

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))



#############################################################################################

# Math

# 최대공약수 구할 때 math library의 gcd() 함수 이용

import math

def lcm(a, b):
    return a*b//math.gcd(a, b)

a=21
b=14

print(math.gcd(21, 14))
print(lcm(21, 14))

