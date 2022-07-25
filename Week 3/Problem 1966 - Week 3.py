# 백준 1966

# 문제

# 프린터 기기는 인쇄하고자 하는 문서를 인쇄 명령을 받은 순서대로 인쇄한다. 여러 개의 문서가 쌓인다면 Queue 자료 구조에 쌓여서
# FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는
# 다음과 같은 조건에 따라 인쇄를 하게 된다.

# 1. 현재 Queue의 가장 앞에 잇는 문서의 '중요도'를 확인한다.
# 2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치한다.
# 그렇지 않다면 바로 인쇄를 한다.
# Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다.

# 입력 : 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
# 출력 : 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1<=N<=100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서
# 몇 번째에 놓여 있는지를 나타내는 정수 (0<=M<N)이 주어진다. 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개의 중요도가 차례대로 주어진다.
# 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

# 출력 : 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.


import sys

T = int(input())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())

    impo = list(map(int, sys.stdin.readline().split()))

    target_num = impo[M]

    impo[M] = 0
    count = 0

    while True:

        a = impo[0]

        if impo[0] == 0:

            if target_num >= max(impo) or len(impo) == 1:
                count += 1
                break

            else:
                impo.pop(0)
                impo.append(a)


        elif a == max(impo) and a >= target_num:
            impo.pop(0)
            count += 1

        else:
            impo.pop(0)
            impo.append(a)

    print(count)


# enumerate : index도 같이 출력해주는 함수

