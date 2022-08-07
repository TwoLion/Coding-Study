# 바닥 공사

# 문제

# 가로의 길이가 N, 세로의 길이가 2인 직사각형 형태의 얇은 바닥이 있다. 태일이는 이 얇은 바닥을
# 1x2의 덮개, 2x1의 덮개, 2x2의 덮개를 이용해 채우고자 한다.
# 이때 바닥을 채우는 모든 경우의 수를 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 N이 주어진다. (1<=N<=1000)
# 출력 : 첫째 줄에 2X N 크기의 바닥을 채우는 방법의 수를 796796으로 나눈 나머지를 출력한다.

N = int(input())

d =[0]*(N+1)

d[1] = 1
d[2] = 3

for i in range(3, N+1):

    d[i] = d[i-1]+2*d[i-2]

print(d[N]%796796)