# 백준 4673

# 문제

# 셀프 넘버는 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수라고 정의하자.
# 양의 정수 n이 주어졌을 대, 이 수를 시작해서 n, d(n), d(d(n)), ...과 같은 무한 수열을 만들 수 있다.
# n을 d(n)의 생성자라고 한다.
# 생성자가 없는 숫자를 셀프 넘버라고 한다.
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

# 입력 : 없음

# 출력 : 10,000보다 작거나 같은 셀프넘버를 한 줄에 하나씩 증가하는 순서로 출력한다.

result = []

def dn(num):
    result = list(str(num))
    return (num + sum(map(int, result)))

for i in range(1, 10001):
    result.append(dn(i))

result = set(result)
num_10000 =set(range(1, 10001))

final = list(num_10000-result)
final.sort()

for i in final:
    print(i)