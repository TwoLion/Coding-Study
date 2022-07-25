# 백준 2615

# 문제

# 바둑판에는 19개의 가로줄과 19개의 세로줄이 그려져 있는데 가로줄은 위에서부터 아래로 1번, 2번, ..., 19번의 번호가 붙고,
# 세로줄은 왼쪽에서부터 오른쪽으로 1번, 2번, ..., 19번의 번호가 붙는다.

# 위의 그림에서와 같이 같은 색의 바둑알이 연속적으로 다섯 알을 놓이면 그 색이 이기게 된다. 하지만 여섯 알 이상이 연속적으로 놓인 경우에는
# 이긴 것이 아니다.

# 입력으로 바둑판의 어떤 상태가 주어졌을 때, 검은색이 이겼는지, 흰색이 이겼는지 또는 아직 승부가 결저오디지 않았는지를 판단하는 프로그램을
# 작성하시오. 단, 검은색과 흰색이 동시에 이기거나 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.

import sys

N = 19


land = []

for _ in range(N):
    land.append(list(map(int, sys.stdin.readline().split())))

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 2 0 0 2 2 2 1 0 0 0 0 0 0 0 0 0 0
0 0 1 2 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0
0 0 0 1 2 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 1 2 2 0 0 0 0 0 0 0 0 0 0 0 0
0 0 1 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 2 1 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 2 1 0 0 0


for i in range(19):
    land[i] = land[i] + [0] * 19
    land.append([0] * 19)


def line_setting(land, case, number):
    result = []
    if case == 'h':
        return(land[number-1][:19])
    elif case == 'v':
        for i in range(19):
            result.append(land[i][number-1])
        return(result)
    else:

        if case=='dd':
            if number<=19:
                for i in range(19):
                        result.append(land[19-number+i][i])
            else:
                num = number-19
                for i in range(19):
                        result.append(land[i][num+i])

        elif case=='ud':
                for i in range(19):
                        result.append(land[i][number-1-i])

        return(result)



test_case = line_setting(land=land, case='ud', number=6)

test_winner(test_case)
def test_winner(case):

    count = 1
    winner=0
    position = 0
    for i in range(len(case)-1):

        if case[i]==case[i+1]:
            count +=1
            print(count)

            if i==len(case)-2:
                if count==5:
                    winner=case[i]
                    position=i-3


        elif case[i]!=case[i+1]:
            if count == 5 and case[i]!=0:
                winner=case[i]
                position = i-3

                count = 1

            else:

                count = 1


    return list((position, winner))

list(test_winner(case=test_case))


def test_all_line(land):



    result_h =[]
    result_v = []
    result_dd = []
    result_ud = []

    for i in range(1, 20):
        test_line = line_setting(land=land, case='h', number=i)
        result = test_winner(case=test_line)
        if result!=[0, 0]:
            result_h.append([i] + result)

    for i in range(1, 20):
        test_line = line_setting(land=land, case='v', number=i)
        result = test_winner(case=test_line)
        if result!=[0, 0]:
            result_v.append([i] + result)

    for i in range(1, 38):
        test_line = line_setting(land=land, case='dd', number=i)
        result = test_winner(case=test_line)
        if result!=[0, 0]:
            result_dd.append([i] + result)

    for i in range(1, 38):
        test_line = line_setting(land=land, case='ud', number=i)
        result = test_winner(case=test_line)
        if result!=[0, 0]:
            result_ud.append([i] + result)

    return([result_h, result_v, result_dd, result_ud])


final = test_all_line(land=land)
final_result =[]
for i in range(4):

    if final[i] != []:
        if i==0:
            final_result = final[i][0]
        elif i==1:
            final_result= final[i][0]
            final_result = [final_result[i][1], final_result[i][0], final_result[i][2]]

        elif i==2:
            final_result = final[i][0]
            if final_result[0]<=19:
                final_result = [19-final_result[0]+(final_result[1]), final_result[1], final_result[2]]
            else:
                final_result = [final_result[1], final_result[0]-18+(final_result[1]-1), final_result[2]]

        else :
            final_result = final[i][0]
            if final_result[0]<=19:
                final_result = [final_result[0]-final_result[1]-3, final_result[1]+4, final_result[2]]
            else:
                num = final_result[0]-18
                final_result = [num-final_result[1]-3, 20-final_result[1]+4, final_result[2]]




print(final_result[2])
print(final_result[0], final_result[1])

final