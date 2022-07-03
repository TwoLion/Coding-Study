
# 기본 입출력
# 모든 프로그램은 적절한 입출력 양식을 가지고 가지고 있음
# 프로그램 동작의 첫 번째 단계는 데이터를 입력 받거나 생성하는 것


# 자주 사용되는 표준 입력 방법

# input() : 한 줄의 문자열을 입력 받는 함수
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용

# ex : 공백을 기준으로 구분된 데이터를 입력 받을 때
# list(map(int, input().split()))

# ex : 공백을 기준으로 구분된 데이터의 개수가 많지 않다면, 다음과 같이 사용
# a, b, c = map(int, input().split())



# 데이터 개수 입력

n = int(input())

print(n)

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# a, b, c를 공백을 기준으로 구분하여 입력
a, b, c = map(int, input().split())


# 빠르게 입력 받기
# sys.stdin.readline() method 이용
# 입력 후 enter가 줄 바꿈 기호로 입력되므로 rstrip() method 함께 이용

import sys

data = sys.stdin.readline().rstrip()
33
print(data)

# 파이썬에서 기본 출력은 print() 함수 이용
# 각 변수를 ,를 이용하여 띄어쓰기로 구분하여 출력 가능
# print()는 출력 이후 줄바꿈 수행
# 줄바꿈 원하지 않는 경우 'end' 속성 이용

# 출력 변수

a=1
b=2
print(a, b)
print(7, end=" ")
print(8, end=" ")

#출력할 변수
answer = 7
print(" 정답은 " + str(answer) + '입니다.')

# f-string

# 중괄호 안에 변수명을 기입하여 간단히 문자열과 정수를 함께 넣을 수 있음

answer = 7
print(f"정답은 {answer}입니다.")

# 16진수 표현법 : '%x'% 숫자로 표현 (소문자) '%X'% : 대문자
# 8진수 표현법 : '%o'% 숫자로 표현 '%O'% : 대문자
# int(a, 진수) : 진수 기준으로 a를 바꾸어줌


a =24
print('%x'%a)

ord('c')