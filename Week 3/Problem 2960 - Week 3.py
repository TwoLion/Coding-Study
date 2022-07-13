# 백준 2960

# 문제

# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 알고리즘이다.
# 이 알고리즘은 다음과 같다.
# 1. 2부터 N가지 모든 정수를 적는다.
# 2. 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# 3. P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 4. 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.

# N과 K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

N, K = map(int, input().split())

count = 0
result = 0
A = range(2, N+1)
B = []

while True:
    a = min(A)
    for i in A:
        if i % a ==0:
            count +=1
            result=i
            if count == K:
                break
        else:
            B.append(i)

    if count == K:
        break
    A = B
    B = []


print(result)

