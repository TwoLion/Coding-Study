# 백준 2012

# 2007년 KOI에 N명의 학생들이 참가하였다. 경시일 전날인 예비소집일에,
# 모든 학생들은 자신이 N명 중에서 몇 등을 할 것인지 예상 등수를 적어서 제출하도록 하였다.
# KOI 조교는 실수로 모든 학생의 프로그램을 날려 버렸다.
# 1등부터 N등까지 동석차 없이 등수를 매겨야 하는 조교는 어쩔 수 없이 각 사람이 제출한 예상 등수를 바탕으로 임의로 등수를 매기기로 했다.
# 자신의 등수를 A등으로 예상하였는데 실제 등수가 B등이 될 경우, 이 사람의 불만도는 A와 B의 차이로 수치화할 수 있다.
# 당신은 N명의 사람들의 불만도의 총 합을 최소로 하면서, 학생들의 등수를 매기려고 한다.
# 각 사람의 예상 등수가 주어졌을 때, 이러한 불만도의 합을 최소로 하는 프로그램을 작성하시오

# 입력 : 첫째 줄에 자연수 N이 주어진다.(1<=N<=500,000) 둘째 줄부터 N개의 줄에 걸쳐 각 사람의 예상 등수가 순서대로 주어진다.
# 예상 등수는 500,000 이하의 자연수이다.
# 첫째 줄에 불만도 합을 최소로 할 때, 그 불만도를 출력한다.

import sys

N = int(sys.stdin.readline())

predict = []

for _ in range(N):
  predict.append(int(sys.stdin.readline()))



predict.sort()
result = 0

for i in range(len(predict)):
  result += abs(predict[i]-(i+1))

print(result)



# for문이나 while을 반복해서 사용하는 경우 input()을 이용하는 경우 시간 초과가 발생할 수 있음
# 이를 위해서 사용하는 함수가 sys.stdin.readline()

# 사용법

# 한 개의 정수를 입력받을 때
# sys.stdin.readline()을 통해 입력받는 경우 입력값\n으로 저장이 됨
# 따라서 int(sys.stdin.readline())을 해주어야 함

# 이외 다른 방법론은 input().split()과 동잃함

# 문자열 n줄을 입력받아 리스트에 저장할 때

n = int(sys.stdin.readline())
data = [sys.stdin.readline().strip() for i in range(n)]

#strip()은 문자열 맨 앞과 맨 끝의 공백문자를 제거함.

# zip 사용해보기


import sys

N = int(input())

result =[]

for _ in range(N):
  result.append(int(sys.stdin.readline()))

A = list(range(1, N+1))
result.sort()

final = sum([abs(i-j) for i, j in zip(result, A)])
print(final)
