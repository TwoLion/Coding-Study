# 문제

# A, B 두 사람이 볼링을 치고 있습니다. 두 사람은 서로 무게가 다른 볼링공을 고르려고 합니다.
# 볼링공은 총 N개가 있으며 각 볼링공마다 무게가 적혀 있고, 공의 번호는 1번부터 순서대로 부여됩니다.
# 또한 같은 무게의 공이 여러 개 있을 수 있지만, 서로 다른 공으로 간주합니다. 볼링공의 무게는 1부터 M까지의 자연수 형태로 존재합니다.

# N개의 공의 무게가 각각 주어질 때, 두 사람이 볼링공을 고르는 경우의 수를 구하는 프로그램을 작성하세요.

# 입력조건 : 첫째 줄에 볼링고의 개수 N, 공의 최대 무게 M이 공백으로 구분되어 각각 자연수 형태로 주어집니다.
# 둘째 줄에 각 볼링공의 무게 K가 공백으로 구분되어 순서대로 자연수 형태로 주어집니다.

# 출력조건 : 첫째 줄에 두 사람이 볼링공을 고르는 경우의 수를 출력합니다.



N, M = map(int, input().split())
a = list(map(int, input().split()))

num = list(set(a))

count_num = []

for i in range(len(num)):
  count_num.append(len([j for j in a if j==num[i]])) 

result = []

for i in range(len(count_num)-1):
  result.append(count_num[i]*sum(count_num[i+1:]))

print(sum(result))


# 다시 풀어보기 - 승연 아이디어 - combination 사용하기
# counter 함수 이용하거나 for 문 이용하여 다시 해보기

array = [0]*m
for i in num :
  array[i] +=1



