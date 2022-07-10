# Example problem


# 큰 수의 법칙
# 문제 : 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙이다. 단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번 초과하여 더해질 수 없는 것이 이 법칙의 특징

# 조건 : 첫째 줄에 N(2<=N<=10000=), M(1<=M<=10000), K(1<=K<=10000)의 자연수가 주어지며, 각 자연수는 공백으로 구분한다.
# 둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는 1 이상 10000 이하의 수로 주어진다.
# 입력으로 주어지는 K는 항상 M보다 작거나 같다.
# 출력 : 첫째 줄에 동빈이의 큰 수의 법칙에 따라 더해진 답을 출력한다.

N, M, K = input().split()
N = int(N)
M = int(M)
K = int(K)

a = list(map(int, input().split()))

a.sort(reverse=True)
maximum = a[0]
second = a[1]
result = 0

for i in range(M):
  if (i+1) % (K+1) == 0:
    result += second
  else:
    result += maximum

print(result)

# Another solution

N, M, K = input().split()
N = int(N)
M = int(M)
K = int(K)

a = list(map(int, input().split()))

a.sort(reverse=True)
maximum = a[0]
second = a[1]
result = 0

if (M) % (K+1) == 0:
  result = (maximum*K+second)*(M//(K+1))

else:
  result = (maximum*K+second)*(M//(K+1)) + maximum*(M % (K+1))

print(result)



# 참고사항
# 1. R에서의 which.min, which.max 뽑는 함수가 쉽지 않다. 따라서 sort를 통해 오름/내림 차순 정렬 후 indexing을 통해 값을 찾자
# 2. 굳이 for 문을 안적어도 된다면 안적는게 베스트이다.