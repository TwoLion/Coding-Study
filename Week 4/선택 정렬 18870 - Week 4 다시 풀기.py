# 백준 18870 (좌표 압축)

# 문제

# 수직선 위에 N개의 좌표 X_1, ..., X_N이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.
# X_i를 좌표 압축한 결과 X'_i의 값은 X_i>X_j를 만족하는 서로 다른 좌표의 개수와 같아야 한다.
# X_1, X_2, ..., X_N에 좌표 압축을 적용한 결과 X_1', X_2', ..., X_N'를 출력해보자.

# 입력 : 첫째 줄에 N이 주어진다.
# 둘째 줄에는 공백 한 칸으로 구분된 X_1, ..., X_N이 주어진다.

# 출력 : 첫째 줄에 X'_1, X'_2, ..., X_'N을 공백 한 칸으로 구분해서 출력한다.

# 제한 : 1<=N<=1,000,000
# -10^9 <=X_i <=10^9


N = int(input())

number = list(map(int, input().split()))


count = sorted(list(set(number)))

dic = {count[i] : i for i in range(len(count))}


for i in number:
    print(dic[i], end=' ')
