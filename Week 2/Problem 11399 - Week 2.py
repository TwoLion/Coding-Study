# 백준 11399

# 인하 은행에는 ATM이 1대밖에 없다. 지금 이 ATM 앞에 N명의 사람들이 줄을 서있다. 사람은 1번부터 N번까지 번호가 매겨져 있으며, i번 사람이 돈을 인출하는데 걸리는 시간은 P_i분이다.
# 줄을 서 있는 사람의 수 N과 각 사람이 돈을 인출하는데 걸리는 시간 P_i가 주어졌을 때, 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 사람의 수 N이 주어진다. 둘째 줄에는 각 사람이 돈을 인출하는데 걸리는 시간 P_i가 주어진다.

# 출력 : 첫째 줄에 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값을 출력한다.


N = int(input())

takingtime = list(map(int, input().split()))

takingtime.sort()

result = 0

for i in range(len(takingtime)):
  result += takingtime[i]*(len(takingtime)-i)


print(result)
