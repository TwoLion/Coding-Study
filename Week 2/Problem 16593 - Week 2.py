# 백준 16953

# 문제

# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

# 1. 2를 곱한다.
# 2. 1을 수의 가장 오른쪽에 추가한다.

# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

# 입력 : 첫째 줄에 A, B(1<=A<B<=10^9)가 주어진다.

# 출력 : A를 B로 바꾸는데 필요한 연산의 최솟값에 1을 더한 값을 출력한다. 만들 수 없는 경우에는 -1을 출력한다.


A, B = map(int, input().split())

result = []

while B > 1 :
  if B%10 == 1 :
    B = (B-1)//10
  elif B%2 == 0 :
    B = B//2

  else:
    B = -1


  result.append(B)

  if B==A:
    break


if B==-1 or A not in result:
  print(-1)

else:
  print(len(result)+1)