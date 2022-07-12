# sys.stdin.readline()

# 반환값은 글자값\n으로 반환됨
# \n을 없애주기 위해 sys.stdin.readline().rstrip()

# rstrip()은 오른쪽 공백, \n을 없애주고, lstrip()은 왼쪽 공백, \n을 없애주고, strip()은 양쪽 공백, \n을 없애줌.

import sys

print(sys.stdin.readline())
print(sys.stdin.readline().rstrip())
print(sys.stdin.readline().strip())


#