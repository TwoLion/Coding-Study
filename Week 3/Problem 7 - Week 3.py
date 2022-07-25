# 문제 Q9

# 어피치는 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서
# 표현하는 알고리즘을 공부하고 있습니다.
# aabbaccc의 경우 2a2ba3c와 같이 표현가능한데, 이 경우 반복되는 문자가 적은 경우 압축률이 낮다는 단점이 있습니다.
# 어피치는 이러한 단점을 해결하기 위해 문자열을 1개 이상의 단위로 잘라서 압축하여 더 짧은 문자열로 표현할 수 있는지 방법을
# 찾아보려고 합니다.
# 예를 들어, 'ababcdcdababcdcd'의 경우 문자를 1개 단위로 자르면 전혀 압축되지 않지만, 2개 단위로 잘라서 압축한다면
# '2ab2cd2ab2cd'로 표현할 수 있습니다. 다른 방법으로 8개 단위로 잘라서 압축한다면 '2ababcdcd'로 표현할 수 있으며,
# 이 때가 가장 짧게 압축하여 표현할 수 있는 방법입니다.
# 다른 예로 'abcabcdede'와 같은 경우 문자를 2개 단위로 짤라서 압축하면 'abcabc2de'가 되지만, 3개 단위로 자른다면 '2abcdede'가 되어
# 3개 단위가 가장 짧은 압축 방법이 됩니다. 이때 3개 단위로 자르고 마지막에 남는 문자열은 그대로 붙여주면 됩니다.

# 압축할 문자열 s가 매개변수로 주어질 때, 위에 설명한 방법으로 1개이상 단위로 문자열을 잘라 압축하여 표현한 문자열 중 가장 짧은 것의
# 길이를 return 하도록 solution 함수를 완성해주세요.

# 제한 사항 : s의 길이는 1 이상 1000 이하
# s는 알파벳 소문자로만 이루어져 있습니다.

def solution(s):
    final_result = s

    for i in range(1, len(s) + 1):

        length = i
        case = len(s) // length
        final = ''
        count = 1

        for j in range(1, case + 1):

            data = s[length * (j - 1):length * j]
            next_data = s[length * j: length * (j + 1)]

            if data == next_data:
                count += 1

            else:
                if count == 1:
                    final += data
                else:
                    final += (str(count) + data)

                count = 1

        if len(s) % length != 0:
            final += s[case * length:]

        if len(final) < len(final_result):
            final_result = final
        else:
            pass

    answer = len(final_result)

    return answer