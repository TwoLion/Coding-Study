# 백준 2839

# 문제

# 상근이는 사탕가게에 설탕을 정확하게 Nkg 배달해야 한다.
# 설탕은 봉지에 담겨져 있는데, 3kg, 5kg 봉지가 있다.
# N킬로그램 배달해야할 때 들고가야할 최소한의 봉지 수는?

# 입력 : 첫째 줄에 N이 주어진다. (3<=N<=5000)
# 출력 : 상근이가 배달하는 봉지의 최소개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면, -1을 출력한다.

N = int(input())

result = 0

if N % 5 ==0 :
  result = N//5

elif N % 5 == 1 :
  result = 2 + (N-6)//5

elif N % 5 == 2 :
  if N == 12:
    result = 4
  elif N < 12:
    result = -1
  else : 
    result = 4 + (N-12)//5

elif N % 5 == 3 :
  result = N//5 + 1

else :
  if N == 9 :
    result = 3
  elif N<9 :
    result = -1
  else :
    result = 3 + (N-9)//5

print(result)