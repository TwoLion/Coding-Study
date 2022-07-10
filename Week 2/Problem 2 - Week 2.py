# Example problem 


# 숫자 카드 게임
# 문제 : 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 룰 : 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다. 이 때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
# 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

# 조건 : 첫째 줄에 숫자 카드들이 놓인 행의 개수 N과 열의 개수 M이 공백을 기준으로 하여 각각 자연수로 주어진다.
# 둘째 줄부터 N개의 줄에 걸쳐 각 카드에 적힌 숫자가 주어진다. 각 숫자는 1 이상 10000 이하의 자연수이다.

# 출력 : 첫째 줄에 게임의 룰에 맞게 선택한 카드에 적힌 숫자를 출력한다.

N, M = map(int, input().split())

matrix=[]

for _ in range(N):
  a = list(map(int, input().split()))
  matrix.append(a)

result = []

for i in range(N):
  result.append(min(matrix[i]))

print(max(result))


# Another solution

N, M = map(int, input().split())

result = []

for i in range(N):
  a = list(map(int, input().split()))
  result.append(min(a))

print(max(result))


# 참고사항
# 문제 상황을 똑같이 만들 필요는 없다. 위 문제의 경우 matrix를 무조건 만들 필요가 없음!
# 물론 필요한 경우 만들 수 있지만, 필요하지 않은 경우 안만들어도 무방함!