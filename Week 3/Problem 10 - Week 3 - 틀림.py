# Q12 기둥과 보 설치

# 문제

# 빙하가 깨지면서 스노우타운에 떠내려온 죠르디는 인생 2막을 위해 주택 건축사업에 뛰어들기로 결정하였습니다.
# 죠르디는 기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 계획인데, 그에 앞서 로봇의 동작을 시뮬레이션 할 수 있는
# 프로그램을 만들고 있습니다.
# 프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데, 기둥과 보는 길이가 1인 선분으로 표현되며
# 다음과 같은 규칙을 가지고 있습니다.

# 기둥은 바닥 위에 있거나 보의 한쪽 끝부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
# 보는 한쪽 끝부분이 기둥 위에 있거나, 또는 양쪽 끝부분이 다른 보와 동시에 연결되어 있어야 합니다.

# 단, 바닥은 벽면의 맨 아래 지면을 말합니다.
# 2차원 벽면은 nxn 크기 정사각 격자 형태이며, 각 격자는 1x1 크기입니다. 맨 처음 벽면은 비어 있는 상태입니다.
# 기둥과 보는 격자 선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있습니다.

# 기둥과 보를 삭제하는 기능도 있는데 기둥과 보를 삭제한 후에 남은 기둥과 보 또한 위 규칙을 만족해야 합니다.
# 만약, 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시됩니다.

# 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때,
# 모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 완성해주세요

# 제한 사항
# n은 5 이상 100 이하인 자연수입니다.
# build_frame의 세로(행) 길이는 1 이상 1000 이하입니다.
# build_frame의 가로(열) 길이는 4입니다.
# build_frame의 원소는 [x, y, a, b] 형태입니다.
# x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# a는 설치 또는 삭제할 구조물의 종류를 나타내며 0은 기둥, 1은 보를 나타냅니다.
# b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1인 설치를 나타냅니다.
# 벽면을 벗어나게 기둥, 보를 설치하는 경우는 없습니다.
# 바닥에 보를 설치하는 경우는 없습니다.
# 구조물은 교차점 좌표를 기준으로 보는 오른쪽, 기둥은 위쪽방향으로 설치 또는 삭제합니다.
# 구조물이 겹치도록 설치하는 경우와 없는 구조물을 삭제하는 경우는 입력으로 주어지지 않습니다.
# 최종 구조물의 상태는 아래 규칙에 맞춰 return해주세요
# return 하는 배열은 가로(열) 길이가 3인 2차원 배열로, 각 구조물의 좌표를 담고 있어야 합니다.
# return 하는 배열의 원소는 [x, y, a] ㅎ형식입니다.
# x, y는 기둥, 보의 교차점 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
# 기둥, 보는 교차점 좌표를 기준으로 오른쪽 또는 위쪽 방향으로 설치되어 있음을 나타냅니다.
# a는 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
# return 하는 배열은 x 좌표 기준으로 오름차순 정렬하며, x 좌표가 같을 경우 y 좌표 기준으로 오름차순 정렬 해주세요
# x, y 좌표가 모두 같은 경우 기둥이 보보다 앞에 오면 됩니다.




# input
# [x좌표, y좌표, 기중(0)/보(1), 건설(1)/삭제(0)]

# output
# [[x좌표, y좌표, 기둥(0)/보(1)]
# 기둥은 좌표 기준 위로 설치
# 보는 좌표 기준 아래로 설치


# 기둥, 보 설치함수
# earlier : output list
def solution(n, build_frame):
    def construct(x, y, case, earlier, size):

        wall = [i[:2] for i in earlier if i[2] == 0]
        ceiling = [i[:2] for i in earlier if i[2] == 1]
        worked = wall + ceiling

        if case == 0:

            if y < 0 or y >= size or x < 0 or x > size:
                return ('no')

            if y == 0:
                return ([x, y, 0])
            else:
                if [x, y - 1] in wall or [x - 1, y] in ceiling or [x + 1, y] in ceiling:
                    return ([x, y, 0])
                else:
                    return ('no')

        else:

            if x < 0 or x >= size or y < 0 or y > size:
                return ('no')

            if [x, y - 1] in wall or [x + 1, y - 1] in wall:
                return [x, y, 1]
            elif [x - 1, y] in ceiling:
                if [x + 1, y] in ceiling:
                    return [x, y, 1]
            else:
                return ('no')

    def destroy(x, y, case, earlier):

        wall = [i[:2] for i in earlier if i[2] == 0]
        ceiling = [i[:2] for i in earlier if i[2] == 1]
        worked = wall + ceiling

        if case == 0:
            if [x, y + 1] in wall:
                if [x, y + 1] in ceiling or [x - 1, y + 1] in ceiling:
                    pass
                else:
                    return ('no')

            if [x, y + 1] in ceiling:
                if [x + 1, y] in wall:
                    pass
                elif [x + 1, y + 1] in ceiling and [x - 1, y + 1] in ceiling:
                    pass
                else:
                    return ('no')

            if [x - 1, y + 1] in ceiling:
                if [x - 1, y] in wall:
                    pass
                elif [x, y + 1] in ceiling and [x - 2, y + 1] in ceiling:
                    pass
                else:
                    return ('no')

            return ([x, y, case])

        else:
            if [x - 1, y] in ceiling:
                if [x - 1, y - 1] in wall or [x, y - 1] in wall:
                    pass
                else:
                    return ('no')

            if [x + 1, y] in ceiling:
                if [x + 1, y - 1] in wall or [x + 2, y - 1] in wall:
                    pass
                else:
                    return ('no')
            return ([x, y, case])

    s = build_frame

    result = []

    for i in s:
        early = result

        if i[3] == 1:

            working = construct(x=i[0], y=i[1], case=i[2], earlier=early, size=n)

            if working == 'no':
                pass
            else:
                result.append(working)


        else:

            des = destroy(x=i[0], y=i[1], case=i[2], earlier=early)

            if des == 'no':
                pass

            elif des not in early:
                pass
            else:
                result.pop(result.index(des))

    result.sort(key=lambda x: (x[0], x[1], x[2]))
    return (result)

