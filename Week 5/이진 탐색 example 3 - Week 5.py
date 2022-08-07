# Q 27

# 문제

# N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬되어 있습니다. 이때 이 수열에서 x가 등장하는 횟수를 계사하세요.
# 수열 {1, 1, 2, 2, 2, 2, 3}이 있을 때 x=2라면, 현재 수열에서 값이 2인 원소가 4개이므로 4를 출력합니다.
# 단, 이 문제는 시간 복잡도 O(logN)으로 알고리즘을 설계하지 않으면 '시간 초과' 판정을 받습ㄴ디ㅏ.

# 입력 : 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력됩니다. (1<=N<=1,000,000), (-10^9<=x<=10^9)
# 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력됩니다. (-10^9 <=각 원소의 값 <=10^9)
# 출력 : 수열의 원소 중에서 값이 x인 원소의 개수를 출력합니다. 단, 값이 x인 원소가 하나도 없다면 -1을 출력합니다.


from bisect import bisect_left, bisect_right


N, x = map(int, input().split())

number = list(map(int, input().split()))

result_left = bisect_left(number, x)
result_right = bisect_right(number, x)


if result_right - result_left ==0 :
    print(-1)

else:
    print(result_right - result_left)

