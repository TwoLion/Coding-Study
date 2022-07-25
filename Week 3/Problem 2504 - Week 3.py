# 백준 2504 (괄호의 값)

# 문제

# 4개의 기호 '(', ')', '[', ']'를 이용해서 만들어지는 괄호열 중에서 올바른 괄호열이란 다음과 같이 정의된다.

# 한 쌍의 괄호로만 이루어진 '()'과 '[]'은 올바른 괄호열이다.
# 만일 x가 올바른 괄호열이면 ' (x)'이나 [x]'도 모두 올바른 괄호열이 된다.
# x와 y 모두 올바른 괄호열이라면 이들을 결합한 xy도 올바른 괄호열이 된다.

# 우리는 어떤 올바른 괄호열 x에 대하여 그 괄호열의 값을 아래와 같이 정의하고 값 x로 표시한다.

# 1. '()' : 2
# 2. '[]' : 3
# 3. '(x)' : 2 X x
# 4. '[x]' : 3 X x
# 올바른 괄호열 x, y가 결합된 xy는 xy = x+y로 계산된다.

# 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력하는 것이다.

# 입력 : 첫째 줄에 괄호열을 나타내는 문자열이 주어진다. 단 그 길이는 1 이상, 30 이하이다.
# 출력 : 첫째 줄에 그 괄호열의 값을 나타내는 정수를 출력한다. 만일 입력이 바르지 못한 괄호열이면 반드시 0을 출력해야 한다.

from collections import Counter

a = input()


a = a.replace('[]', '3').replace('()', '2')

a = a.replace('](', '+').replace(')[', '+').replace('][', '+').replace(')(', '+')

a=a.replace('2(', '2+(').replace('2[', '2+[').replace(')2', ')+2').replace(']2', ']+2')

a=a.replace('3(', '3+(').replace('3[', '3+[').replace(')3', ')+3').replace(']3', ']+3')
a=a.replace('+[', '+3*(').replace('+(', '+2*(').replace('2]', '2)').replace('3]', '3)')


if a[0]=='(' and a[-1]==')':
    a = '2*'+a

elif a[0]=='[' and a[-1]==']':
    a = '3*'+a

print(a)