# 백준 11497(통나무 건너뛰기)

# 문제

# 남규는 통나무를 세워 놓고 건너뛰기를 좋아한다. 그래서 N개의 통나무를 원형으로 세워 놓고 뛰어놀려고 한다.
# 남규는 원형으로 인접한 옆 통나무로 건너뛰는데, 이때 각 인접한 통나무의 높이 차가 최소가 되게 하려 한다.

# 통나무 건너뛰기의 난이도는 인접한 두 통나무 간의 높이의 차의 최댓값으로 결정된다. 난이도가 낮은 배열이 되도록 통나무를 움직여주세요

# 입력 : 입력은 T개의 테스트 케이스로 이루어져 있다. 첫 줄에 T가 주어진다.
# 이어지는 각 줄마다 첫 줄에 통나무의 개수를 나타내는 정수 N(5<=N<=10,000), 둘째 줄에 각 통나무으 ㅣ높이를 나타내는 정수 L_i가 주어진다.
# (1<=L_i<=100,000)

# 출력 : 각 테스트 케이스마다 한 줄에 주어진 통나무들로 만들 수 있는 최소 난이도를 출력하시오.








def mini_level(number):
    number = sorted(number)
    result = [number[0]]*len(number)
    count = 0
    for i in range(0, len(number)):
        if i%2 ==0:
            result[i//2] = number[i]

        else:
            result[-(i//2 +1)] = number[i]

    result.append(result[0])
    count = 0
    for i in range(len(result)-1):
        if count < abs(result[i]-result[i+1]):
            count = abs(result[i]-result[i+1])

    return(count)


T = int(input())

for _ in range(T):

    N = int(input())
    number = list(map(int, input().split()))

    print(mini_level(number=number))
