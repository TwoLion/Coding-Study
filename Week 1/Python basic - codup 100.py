# 기초 입출력

#print, string 기초

#print(a, b)로 출력하는 경우, a와 b 사이 공백이 발생

print('a', 'b')

#줄바꿈은 엔터후 다시 print 작성 또는 \n 사용, 두 줄쓰되 줄바꿈 하기 싫은 경우 end 변수 사용

print('Hello')
print('World')
print('Hello\nWorld')

print('a', end='')
print('b', end='')

#작은 따옴표 사용방법은 "'" 또는 \' 사용

print('\'a\'')
print("'a'")

# 큰 따옴표 사용방법은 '"' 또는 \" 사용

print('"a"')
print("\"a\"")

#\ 출력하려면 \\로 출력

print('\\')

#ex

print('print\"Hello\\nWorld\"')

# print 함수의 sep method는 , 사이 값들을 sep에서 제시한 값으로 구분해서 나타내줌

print('a', 'b', sep=':')

# 입력

#input() 함수 사용

# 타입 바꾸기

# int() : 정수 타입
# float() : 실수 타입

f = input()
f = float(f)
print(f)

# split 함수
# input().split() : 공백 기준으로 입력된 값들을 나누어 자른다. split에 string을 제시하면 제시한 string 기준으로 자름

#ex

a, b = input().split() #두개만 입력 가능
input().split() # 여러개 입력 가능, 대신 지정이 안됨.


##############################################################################################

# 연산

# 소숫점이하 자리 변환 방법

# 1. round 함수 사용 - 반올림에 0 있으면 표현 안함
# 2. format(수, '.2f') - 무조검 표현함


# bool 함수
# 입력된 식이나 값을 평가해 불 형의 값(True or False)로 출력
# 정수값 0은 False, 이외의 값은 True으로 출력

# not 함수
# bool 값에 not을 붙이면 반대 경우를 표현함



# bit 단위 연산자
# ~ (bitwise not), & (bitwise and), | (bitwise or), ^ (bitwise xor), << (bitwise left shift), >> (bitwise right shift)


h, w = input().split()
h = int(h); w=int(w)

D=[[0 for i in range(w)] for j in range(h)]


n = int(input())

for _ in range(n):
    l, d, x, y = input().split()
    l = int(l); d = int(d); x = int(x); y = int(y)

    if d==0:
        for i in range(l):
            D[x-1][y-1+i]=1
    else:
        for i in range(l):
            D[x-1+i][y-1]=1


for i in range(h):
    for j in range(w):
        print(D[i][j], end=' ')
    print()


D = []
for i in range(10):
    a = input().split()
    for j in range(10):
        a[j] = int(a[j])
    D.append(a)



start = [1, 1]

D[start[0]][start[1]]=9


while D[start[0]][start[1]]!=2:
    if D[start[0]][start[1]+1] !=1:
        if D[start[0]][start[1]+1] == 2:
            D[start[0]][start[1] + 1] = 9
            break
        else:
            D[start[0]][start[1] + 1] = 9
            start[1]+=1
    elif D[start[0]+1][start[1]]!=1:
        if D[start[0]+1][start[1]] == 2:
            D[start[0]+1][start[1]] = 9
            break
        else:
            D[start[0]+1][start[1]] = 9
            start[0] += 1

    else:
        break



for i in range(10):
    for j in range(10):
        print(D[i][j], end=' ')
    print()