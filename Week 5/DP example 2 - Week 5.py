# 개미전사

# 문제

# 개미 전사는 부족한 식량을 충당하고자 메뚜기 마을의 식량창고를 몰래 공격하려고 한다.
# 메뚜기 마을에는 여러 개의 식량창고가 있는데 식량탕고는 일직선으로 이어져 있다.
# 각 식량창고에는 정해진 수의 식량을 저장하고 있으며 개미 전사는 식량창고를 선택적으로 약탈하여 식량을 빼앗을 예정이다.
# 이때 메뚜기 정찰병들은 일직선상에 존재하는 식량창고 중에서 서로 인접한 식량창고가 공격받으면 바로 알아챌 수 있다.
# 따라서 개미 전사가 정찰병에게 들키지 않고 식량창고를 약탈하기 위해서는 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 한다.
# 개미 전사는 식량창고가 이렇게 일직선상일 때 최대한 많은 식량을 얻기를 원한다.
# 개미 전사를 위해 식량창고 N개에 대한 정보가 주어졌을 때 얻을 수 있는 식량의 최댓값을 구하는 프로그램을 작성하시오.

N = int(input())

store = list(map(int, input().split()))

d = [0]*N

d[0]=store[0]
d[1]=max(store[1], store[0])

for i in range(2, N):

    d[i] = max(d[i-1], d[i-2]+store[i])


print(d[N-1])